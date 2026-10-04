"""
Devin bridge — hand a programming request from JARVIS to Devin.

Say "Jarvis, sag Devin: ..." and JARVIS starts a Devin session that works on
the configured GitHub repository and opens a pull request. Starting a session
costs Devin usage, so it always goes through the on-screen confirmation gate;
checking status and sending follow-up messages do not.

Needs a Devin Personal Access Token (Settings → Devin API → PATs) and the
organization ID, both entered under ⚙ → PLUGINS. Uses the v3 API:
https://docs.devin.ai/api-reference/personal-access-tokens
"""

from __future__ import annotations

import webbrowser

import requests

from memory.config_manager import get_plugin_config, save_plugin_config

NS = "devin_bridge"
API = "https://api.devin.ai/v3/organizations"
TIMEOUT = 20

PLUGIN = {
    "name": "devin_bridge",
    "description": (
        "Hand a software/programming request to Devin, the AI software engineer, "
        "who then writes the code and opens a pull request. Use when the user says "
        "things like 'sag Devin', 'Devin soll', 'lass Devin ... programmieren', "
        "'ask Devin to build', or wants a NEW feature, plugin, website or app built "
        "for JARVIS. action='start' with the full request in 'task' starts a new job; "
        "action='status' reports how the last Devin job is going; action='message' "
        "sends extra instructions in 'task' to the last job. Do NOT use this for "
        "things JARVIS can do itself right now (opening apps, searching, files)."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "action": {"type": "STRING", "enum": ["start", "status", "message"],
                       "description": "start a new job, check status, or send a follow-up"},
            "task": {"type": "STRING",
                     "description": "What Devin should build or change, in the user's words "
                                    "and as complete as possible (for start/message)"},
        },
        "required": ["action"],
    },
}


def _cfg() -> dict:
    c = get_plugin_config(NS)
    return {
        "token": str(c.get("token") or "").strip(),
        "org_id": str(c.get("org_id") or "").strip(),
        "repo": str(c.get("repo") or "madshadowtest/Mark-LV").strip(),
        "open_browser": bool(c.get("open_browser", True)),
        "last_session": str(c.get("last_session") or ""),
    }


def _req(method: str, path: str, cfg: dict, json: dict | None = None) -> dict:
    r = requests.request(method, f"{API}/{cfg['org_id']}{path}", json=json,
                         timeout=TIMEOUT,
                         headers={"Authorization": f"Bearer {cfg['token']}"})
    if r.status_code in (401, 403):
        raise RuntimeError("Devin lehnt den Zugang ab - Token oder Organisations-ID prüfen")
    r.raise_for_status()
    return r.json() if r.content else {}


def _prompt(task: str, repo: str) -> str:
    return (
        f"Request from the user, spoken to their JARVIS voice assistant:\n\n"
        f"\"{task}\"\n\n"
        f"Repository: https://github.com/{repo} (JARVIS / Mark LV, Python + PyQt6). "
        f"Implement it on a new branch and open a pull request against main. "
        f"Prefer a drop-in plugin in plugins/ when the request is a new capability. "
        f"Never commit config/api_keys.json or memory files. Keep CRLF line endings. "
        f"The user is not a developer: communicate with them in simple German."
    )


def _start(task: str, cfg: dict, player=None) -> str:
    data = _req("POST", "/sessions", cfg, {
        "prompt": _prompt(task, cfg["repo"]),
        "title": f"JARVIS: {task[:70]}",
        "tags": ["jarvis"],
    })
    sid, url = data.get("session_id", ""), data.get("url", "")
    if sid:
        save_plugin_config(NS, {"last_session": sid})
    if url and cfg["open_browser"]:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    if player:
        try:
            player.write_log(f"JARVIS: Devin arbeitet daran: {url}")
        except Exception:
            pass
    return f"Devin started: {url}"


def _status(cfg: dict) -> str:
    if not cfg["last_session"]:
        return "There is no Devin job yet. Ask the user what Devin should build."
    d = _req("GET", f"/sessions/{cfg['last_session']}", cfg)
    prs = [p.get("pr_url") for p in d.get("pull_requests") or [] if p.get("pr_url")]
    parts = [f"Devin job '{d.get('title') or ''}': status {d.get('status')}"
             f" ({d.get('status_detail') or '-'})."]
    if prs:
        parts.append("Pull request ready to review and merge: " + ", ".join(prs))
    if d.get("status_detail") == "waiting_for_user":
        parts.append("Devin is waiting for an answer from the user in the Devin app.")
    parts.append(f"Session: {d.get('url', '')}")
    return " ".join(parts) + " Tell the user briefly, in their language."


def _message(task: str, cfg: dict) -> str:
    if not cfg["last_session"]:
        return "There is no Devin job to message yet - start one first."
    _req("POST", f"/sessions/{cfg['last_session']}/messages", cfg, {"message": task})
    return "Sent the message to Devin."


def run(parameters: dict, player=None, session_memory=None) -> str:
    action = str(parameters.get("action") or "start").lower()
    task = str(parameters.get("task") or "").strip()
    cfg = _cfg()
    if not cfg["token"] or not cfg["org_id"]:
        return ("The Devin connection is not set up yet. Tell the user to enter the "
                "Devin token and organization ID under settings, PLUGINS, DEVIN.")
    try:
        if action == "status":
            return _status(cfg)
        if action == "message":
            if not task:
                return "Ask the user what to tell Devin."
            return _message(task, cfg)
        if not task:
            return "Ask the user what Devin should build."
        try:
            from core import confirm
        except Exception:
            confirm = None
        if confirm is None:
            return _start(task, cfg, player)
        return confirm.request(
            "devin_start", "Auftrag an Devin senden",
            f"{task[:160]} (verbraucht Devin-Guthaben)",
            lambda: _start(task, cfg, player))
    except Exception as e:
        return f"Talking to Devin failed: {e}"


def _test(values: dict):
    cfg = {"token": str(values.get("token") or "").strip(),
           "org_id": str(values.get("org_id") or "").strip()}
    if not cfg["token"] or not cfg["org_id"]:
        return False, "Token und Organisations-ID eintragen"
    try:
        _req("GET", "/sessions?first=1", cfg)
        return True, "Verbindung zu Devin steht"
    except Exception as e:
        return False, str(e)


PLUGIN_SETTINGS = {
    "namespace": NS,
    "title": "DEVIN",
    "fields": [
        {"key": "token", "label": "Devin Personal Access Token", "type": "password",
         "placeholder": "Devin → Settings → Devin API → PATs"},
        {"key": "org_id", "label": "Organisations-ID", "type": "text",
         "placeholder": "org-..."},
        {"key": "repo", "label": "GitHub-Repository", "type": "text",
         "default": "madshadowtest/Mark-LV"},
        {"key": "open_browser", "label": "Devin im Browser öffnen", "type": "toggle",
         "default": True},
    ],
    "action": {"label": "VERBINDUNG TESTEN", "run": _test},
}
