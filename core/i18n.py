"""German UI text for the HUD.

The upstream UI writes its labels in English directly in ui.py. Rather than
editing hundreds of lines there (and conflicting with every upstream update),
ui.py swaps in thin subclasses of QLabel / QPushButton / QLineEdit / QPainter
that pass every visible string through `t()`. Strings with no entry here are
shown unchanged, so a new upstream label simply appears in English until it is
added below.

Active when "language" in config/api_keys.json is German (the default in this
fork). Set it to "English" to get the original UI back.
"""
from __future__ import annotations

import re

from memory.config_manager import get_language

_GERMAN_NAMES = {"german", "deutsch", "de"}


def is_german() -> bool:
    return get_language().strip().lower() in _GERMAN_NAMES


DE: dict[str, str] = {
    # First-run setup
    "◈  INITIALISATION REQUIRED": "◈  EINRICHTUNG ERFORDERLICH",
    "Configure J.A.R.V.I.S. before first boot.": "Richte J.A.R.V.I.S. vor dem ersten Start ein.",
    "GEMINI API KEY": "GEMINI-API-SCHLÜSSEL",
    "OPERATING SYSTEM": "BETRIEBSSYSTEM",
    "▸  INITIALISE SYSTEMS": "▸  SYSTEME STARTEN",
    # Customise dialog
    "⚙  CUSTOMISE ASSISTANT": "⚙  ASSISTENT ANPASSEN",
    "ASSISTANT NAME": "NAME DES ASSISTENTEN",
    "YOUR NAME  (leave blank for default sir / efendim)": "DEIN NAME  (leer lassen für die Standardanrede)",
    "e.g.  Tony   (leave blank for auto)": "z. B.  Tony   (leer lassen für automatisch)",
    "ASSISTANT VOICE": "STIMME DES ASSISTENTEN",
    "UI COLOUR  —  drag the handle": "FARBE  —  Regler ziehen",
    "#00d4ff   (custom hex colour)": "#00d4ff   (eigene Hex-Farbe)",
    "DEFAULT": "STANDARD",
    "▸  APPLY CHANGES": "▸  ÄNDERUNGEN ÜBERNEHMEN",
    "CANCEL": "ABBRECHEN",
    # Dialogs and panels
    "Select a file for JARVIS": "Datei für JARVIS auswählen",
    "◈  VISUAL INPUT": "◈  VISUELLE EINGABE",
    "🧩  PLUGIN MANAGER": "🧩  PLUGIN-VERWALTUNG",
    "No plugins found in /plugins.": "Keine Plugins in /plugins gefunden.",
    "BROKEN": "DEFEKT",
    "CLOSE": "SCHLIESSEN",
    "✕  CLOSE": "✕  SCHLIESSEN",
    "⚠  CONFIRM": "⚠  BESTÄTIGEN",
    "▸  CONFIRM": "▸  BESTÄTIGEN",
    "🎧  AUDIO DEVICES": "🎧  AUDIOGERÄTE",
    "Applying reconnects the session. Your conversation is kept.":
        "Beim Übernehmen wird die Sitzung neu verbunden. Dein Gespräch bleibt erhalten.",
    "▸  APPLY": "▸  ÜBERNEHMEN",
    "🧠  WHAT JARVIS REMEMBERS": "🧠  WAS JARVIS SICH MERKT",
    "Nothing stored yet.": "Noch nichts gespeichert.",
    "Forget this": "Vergessen",
    "◈  CLIPBOARD DETECTED": "◈  ZWISCHENABLAGE ERKANNT",
    "TRANSLATE": "ÜBERSETZEN",
    "SUMMARISE": "ZUSAMMENFASSEN",
    "EXPLAIN": "ERKLÄREN",
    "FIX": "KORRIGIEREN",
    "▸  SAVE": "▸  SPEICHERN",
    "ON": "AN",
    "OFF": "AUS",
    "Testing…": "Teste…",
    "Saved ✓": "Gespeichert ✓",
    "NEW KEY": "NEUER SCHLÜSSEL",
    "DISMISS": "AUSBLENDEN",
    "DISMISS  ✕": "AUSBLENDEN  ✕",
    "CONNECTED": "VERBUNDEN",
    "Phone connected — JARVIS ready": "Handy verbunden – JARVIS bereit",
    "◈  CAMERA FEED": "◈  KAMERABILD",
    "🔇  SOUND OFF": "🔇  TON AUS",
    "🔊  SOUND ON": "🔊  TON AN",
    "Video playback is not available in this Qt install.":
        "Videowiedergabe ist in dieser Qt-Installation nicht verfügbar.",
    "FINISH  →": "FERTIG  →",
    "NEXT  →": "WEITER  →",
    "your answer": "deine Antwort",
    # Main window
    "Settings & Controls": "Einstellungen & Steuerung",
    "Setup — things you set once": "Einrichtung – einmalige Einstellungen",
    "Controls — the everyday switches": "Steuerung – die Alltagsschalter",
    "◈ SYS MONITOR": "◈ SYSTEMMONITOR",
    "No file loaded — drop or click above to upload":
        "Keine Datei geladen – oben ablegen oder klicken zum Hochladen",
    "✋  INTERRUPT  [ESC]": "✋  UNTERBRECHEN  [ESC]",
    "🎙  MICROPHONE ACTIVE": "🎙  MIKROFON AKTIV",
    "🔇  MICROPHONE MUTED": "🔇  MIKROFON STUMM",
    "Type a command or question…": "Befehl oder Frage eingeben…",
    "Personal AI Assistant": "Persönlicher KI-Assistent",
    # Setup drawer
    "◈ SETUP": "◈ EINRICHTUNG",
    "◉  REMOTE CONTROL": "◉  FERNSTEUERUNG",
    "⊞  CREATE DESKTOP SHORTCUT": "⊞  DESKTOP-VERKNÜPFUNG ERSTELLEN",
    "◉  AUTO-START: OFF": "◉  AUTOSTART: AUS",
    "◉  AUTO-START: ON": "◉  AUTOSTART: AN",
    "🧠  MEMORY": "🧠  GEDÄCHTNIS",
    "⚙  PLUGIN SETTINGS": "⚙  PLUGIN-EINSTELLUNGEN",
    # Controls drawer
    "◈ CONTROLS": "◈ STEUERUNG",
    "⛶  FULLSCREEN  [F11]": "⛶  VOLLBILD  [F11]",
    "☀  MORNING BRIEF: ON": "☀  MORGEN-BRIEFING: AN",
    "☀  MORNING BRIEF: OFF": "☀  MORGEN-BRIEFING: AUS",
    "🎙  WAKE WORD": "🎙  WECKWORT",
    "🎙  WAKE WORD: ON": "🎙  WECKWORT: AN",
    "🎙  WAKE WORD: OFF": "🎙  WECKWORT: AUS",
    "⬇  WAKE WORD: DOWNLOAD": "⬇  WECKWORT: HERUNTERLADEN",
    "⬇  DOWNLOADING… (one-time)": "⬇  LADE HERUNTER… (einmalig)",
    "😴  SLEEP NOW": "😴  JETZT SCHLAFEN",
    "👂  WAKE NOW": "👂  JETZT AUFWACHEN",
    "🎚  PUSH-TO-TALK: OFF": "🎚  PUSH-TO-TALK: AUS",
    "🎚  PUSH-TO-TALK: ON": "🎚  PUSH-TO-TALK: AN",
    "Microphone stays closed until you hold the key — nothing is sent while you are not holding it.":
        "Das Mikrofon bleibt zu, bis du die Taste hältst – solange du sie nicht hältst, wird nichts gesendet.",
    "Hold a key to talk instead of streaming the mic continuously.":
        "Taste gedrückt halten zum Sprechen, statt das Mikrofon dauerhaft zu übertragen.",
    "🧑  HUD: ANIMATED FACE": "🧑  HUD: ANIMIERTES GESICHT",
    "◉  HUD: REACTOR CORE": "◉  HUD: REAKTORKERN",
    "An animated head that speaks your words and shows what JARVIS is doing. Tap to switch to the reactor core.":
        "Ein animierter Kopf, der spricht und zeigt, was JARVIS gerade tut. Tippen, um zum Reaktorkern zu wechseln.",
    "A reactor core that turns with the state and moves with your voice. Tap to switch to the animated head.":
        "Ein Reaktorkern, der sich je nach Zustand dreht und auf deine Stimme reagiert. Tippen, um zum animierten Kopf zu wechseln.",
    # File drop zone (painted)
    "Drop file here  or  Click to Browse": "Datei hier ablegen  oder  klicken zum Auswählen",
    "Images · Video · Audio · PDF · Docs · Code · Data": "Bilder · Video · Audio · PDF · Dokumente · Code · Daten",
    "Release to load": "Loslassen zum Laden",
    # Activity log
    "SYS: Interrupted — listening...": "SYS: Unterbrochen – höre zu...",
    "SYS: I'm asleep — say 'Hey Jarvis' or tap WAKE NOW first.":
        "SYS: Ich schlafe – sag zuerst „Hey Jarvis“ oder tippe auf JETZT AUFWACHEN.",
    "SYS: Shutdown requested.": "SYS: Herunterfahren angefordert.",
    "SYS: Phone connected via Remote Dashboard.": "SYS: Handy über das Fern-Dashboard verbunden.",
    "SYS: Could not fetch the news for the briefing.":
        "SYS: Nachrichten für das Briefing konnten nicht geladen werden.",
}

_STATES = {
    "MUTED": "STUMM", "SPEAKING": "SPRICHT", "THINKING": "DENKT NACH",
    "PROCESSING": "VERARBEITET", "LISTENING": "HÖRT ZU", "SLEEPING": "SCHLÄFT",
    "INITIALISING": "STARTET",
}

DE_PATTERNS: list[tuple[re.Pattern, object]] = [
    (re.compile(r"^(\S+)  (" + "|".join(_STATES) + r")$"),
     lambda m: f"{m.group(1)}  {_STATES[m.group(2)]}"),
    (re.compile(r"^Auto-detected: (.+)$"), r"Automatisch erkannt: \1"),
    (re.compile(r"^(.+)  \(not connected\)$"), r"\1  (nicht verbunden)"),
    (re.compile(r"^Key expires in  (.+)$"), r"Schlüssel läuft ab in  \1"),
    (re.compile(r"^(\d+) stored facts — newest first\. Nothing here is sent anywhere; "
                r"it lives in memory/long_term\.json on this machine\.$"),
     r"\1 gespeicherte Fakten – neueste zuerst. Nichts davon wird irgendwohin gesendet; "
     r"es liegt in memory/long_term.json auf diesem Rechner."),
    (re.compile(r"^(.+)  ·  (.+)  ·  Tell (.+) what to do with it$"),
     r"\1  ·  \2  ·  Sag \3, was damit passieren soll"),
    (re.compile(r"^SYS: Sleeping — (.+)\. Say 'Hey Jarvis' to wake me\.$"),
     r"SYS: Schlafe – \1. Sag „Hey Jarvis“, um mich zu wecken."),
    (re.compile(r"^SYS: Awake — (.+)\.$"), r"SYS: Wach – \1."),
    (re.compile(r"^You: "), "Du: "),
]

_ACTIVE = is_german()


def t(text):
    """Translate one visible string; anything unknown is returned unchanged."""
    if not _ACTIVE or not isinstance(text, str) or not text:
        return text
    hit = DE.get(text)
    if hit is not None:
        return hit
    for pattern, repl in DE_PATTERNS:
        new, n = pattern.subn(repl, text, count=1)
        if n:
            return new
    return text


def _tr_args(args):
    return tuple(t(a) if isinstance(a, str) else a for a in args)


def _localized(cls, translate_text: bool):
    def __init__(self, *args, **kwargs):
        cls.__init__(self, *(_tr_args(args) if translate_text else args), **kwargs)

    ns = {
        "__init__": __init__,
        "setToolTip": lambda self, s: cls.setToolTip(self, t(s)),
    }
    if translate_text:
        ns["setText"] = lambda self, s: cls.setText(self, t(s))
    if hasattr(cls, "setPlaceholderText"):
        ns["setPlaceholderText"] = lambda self, s: cls.setPlaceholderText(self, t(s))
    return type(cls.__name__, (cls,), ns)


def localize_widgets(QLabel, QPushButton, QLineEdit):
    """Return German-speaking drop-ins for the three widget classes ui.py uses
    for visible text. A QLineEdit's own text is user input and is left alone."""
    if not _ACTIVE:
        return QLabel, QPushButton, QLineEdit
    return (_localized(QLabel, True), _localized(QPushButton, True),
            _localized(QLineEdit, False))


def localize_painter(QPainter):
    """Return a QPainter whose drawText() translates painted labels."""
    if not _ACTIVE:
        return QPainter

    def drawText(self, *args):
        return QPainter.drawText(self, *_tr_args(args))

    return type("QPainter", (QPainter,), {"drawText": drawText})

# Labels whose text is assembled in ui.py (panel headers, status tiles, date).
DE.update({
    "▸ ACTIVITY LOG": "▸ AKTIVITÄTSPROTOKOLL",
    "▸ FILE UPLOAD": "▸ DATEI-UPLOAD",
    "▸ COMMAND INPUT": "▸ BEFEHLSEINGABE",
    "AI CORE\nACTIVE": "KI-KERN\nAKTIV",
    "SEC\nCLEARED": "SICHERHEIT\nOK",
    "[F4] Mute  ·  [F11] Fullscreen": "[F4] Stumm  ·  [F11] Vollbild",
    "A Friendly Assistant": "Ein freundlicher Assistent",
    "Personal AI Assistant": "Persönlicher KI-Assistent",
})

_DAYS = {"Mon": "Mo", "Tue": "Di", "Wed": "Mi", "Thu": "Do", "Fri": "Fr",
         "Sat": "Sa", "Sun": "So"}
_MONTHS = {"Jan": "Jan", "Feb": "Feb", "Mar": "Mär", "Apr": "Apr", "May": "Mai",
           "Jun": "Jun", "Jul": "Jul", "Aug": "Aug", "Sep": "Sep", "Oct": "Okt",
           "Nov": "Nov", "Dec": "Dez"}

DE_PATTERNS.extend([
    (re.compile(r"^PROTOCOL\n(.+)$"), r"PROTOKOLL\n\1"),
    (re.compile(r"^(" + "|".join(_DAYS) + r") (\d{2}) (" + "|".join(_MONTHS) + r") (\d{4})$"),
     lambda m: f"{_DAYS[m[1]]} {m[2]}. {_MONTHS[m[3]]} {m[4]}"),
])

DE.update({
    "🌸  HUD: ANIME FACE": "🌸  HUD: ANIME-GESICHT",
    "SYS: HUD switched to the anime face.": "SYS: HUD zeigt jetzt das Anime-Gesicht.",
    "SYS: HUD switched to the animated face.": "SYS: HUD zeigt jetzt das animierte Gesicht.",
    "SYS: HUD switched to the reactor core.": "SYS: HUD zeigt jetzt den Reaktorkern.",
    "SYS: Text size saved — restart JARVIS to apply it.":
        "SYS: Schriftgröße gespeichert – wirkt nach einem Neustart von JARVIS.",
})
DE_PATTERNS.append((re.compile(r"^🔠  TEXT SIZE: (\d+)%$"), r"🔠  SCHRIFTGRÖSSE: \1 %"))
