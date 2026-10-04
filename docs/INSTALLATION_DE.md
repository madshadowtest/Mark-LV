# Jarvis (Mark LV) auf Windows installieren

Diese Anleitung ist für Windows 10 und 11 geschrieben. Programmierkenntnisse brauchst du keine. Rechne mit etwa 20 Minuten, den größten Teil davon läuft der Download.

**Du brauchst:** einen Windows-PC mit Mikrofon und Lautsprechern und eine Internetverbindung. Ein Google-Konto ist nur nötig, wenn du noch keinen Gemini-Schlüssel hast (siehe Schritt 2).

---

## Schritt 1: Python installieren (einmalig)

Jarvis ist in der Programmiersprache Python geschrieben. Damit es auf deinem PC läuft, muss Python einmal installiert werden.

1. Öffne https://www.python.org/downloads/windows/
2. Such den neuesten Eintrag **„Python 3.12.x“** und klick auf **„Windows installer (64-bit)“**.
3. Starte die heruntergeladene Datei.
4. **Wichtig:** Setz unten im ersten Fenster den Haken bei **„Add python.exe to PATH“**.
5. Klick auf **„Install Now“** und warte, bis „Setup was successful“ erscheint.

> Hast du für Mark XXXIX schon Python installiert? Dann prüfst du die Version so: Drück die Windows-Taste, tipp `cmd` ein und drück Enter. Gib im schwarzen Fenster `py --version` ein. Steht dort 3.11, 3.12 oder 3.13, kannst du Schritt 1 überspringen.

## Schritt 2: Gemini-Schlüssel bereithalten

Jarvis nutzt Googles KI „Gemini“ und braucht dafür einen kostenlosen Schlüssel.

- **Du hast schon einen von Mark XXXIX?** Dann kannst du ihn weiterverwenden. Öffne den alten Ordner `C:\Users\Garre\Desktop\Mark-XXXIX-OR-main\config` und mach einen Rechtsklick auf `api_keys.json` → **Öffnen mit** → **Editor**. Kopier den Text hinter `"gemini_api_key"`, also das, was zwischen den Anführungszeichen steht und mit `AIza` beginnt.
- **Noch keinen Schlüssel?** Öffne https://aistudio.google.com/app/apikey, melde dich mit Google an und klick auf **„Create API key“**. Kopier den Schlüssel.

> Behandle den Schlüssel wie ein Passwort. Schick ihn niemandem, auch nicht mir.

## Schritt 3: Jarvis herunterladen

1. Öffne deine Kopie: https://github.com/madshadowtest/Mark-LV
2. Klick auf den grünen Button **„Code“** und dann auf **„Download ZIP“**.
3. Rechtsklick auf die heruntergeladene ZIP-Datei → **„Alle extrahieren…“** → als Ziel den **Desktop** wählen → **„Extrahieren“**.
4. Auf dem Desktop liegt jetzt der Ordner **`Mark-LV-main`**.

## Schritt 4: Jarvis installieren (einmalig)

1. Öffne den Ordner `Mark-LV-main`. Darin siehst du Dateien wie `main.py` und `setup.py`.
2. Klick oben in die **Adresszeile** des Explorers (dort, wo der Pfad steht), tipp `cmd` ein und drück **Enter**. Es öffnet sich ein schwarzes Fenster, das schon im richtigen Ordner ist.
3. Tipp diesen Befehl ein und drück Enter:

   ```
   py -3.12 setup.py
   ```

4. Jetzt laufen viele Zeilen durch, das kann **5 bis 15 Minuten** dauern. Fertig ist es, wenn **„✅ Setup complete!“** erscheint.

> Wenn du statt 3.12 eine andere Python-Version hast, ersetz `3.12` entsprechend, zum Beispiel durch `py -3.13 setup.py`.

## Schritt 5: Jarvis starten

1. Gib im selben schwarzen Fenster ein:

   ```
   py -3.12 main.py
   ```

2. Beim ersten Start erscheint das Fenster **„EINRICHTUNG ERFORDERLICH“**:
   - Füg bei **GEMINI-API-SCHLÜSSEL** deinen Schlüssel ein (Strg+V).
   - Wähl bei **BETRIEBSSYSTEM** den Eintrag **Windows**.
   - Klick auf **„▸ SYSTEME STARTEN“**.
3. Fragt Windows nach dem **Mikrofon** oder der **Firewall**, klick auf **Zulassen**.
4. Jarvis begrüßt dich. Sprich ihn einfach auf Deutsch an.

> Das schwarze Fenster muss offen bleiben, solange Jarvis läuft. Wenn du es schließt, beendest du auch Jarvis.

## Schritt 6: Bequemer starten (optional)

Klick in Jarvis oben auf **⚙** und dann auf **„DESKTOP-VERKNÜPFUNG ERSTELLEN“**. Danach startest du Jarvis per Doppelklick auf das Desktop-Symbol, das schwarze Fenster brauchst du dann nicht mehr. Unter **⚙** findest du außerdem **AUTOSTART**, damit Jarvis automatisch mit Windows startet.

Weitere nützliche Schalter:
- **⚙ → ASSISTENT ANPASSEN:** Namen, Anrede, Stimme und Farbe ändern
- **⚙ → FERNSTEUERUNG:** Jarvis vom Handy aus bedienen (QR-Code scannen, Handy und PC müssen im selben WLAN sein)
- **🎛 → WECKWORT:** Jarvis wacht auf, wenn du „Hey Jarvis“ sagst. Das Weckwort selbst ist englisch.

---

## Sprache

Deine Version ist auf **Deutsch** eingestellt, sobald die deutsche Version übernommen ist (siehe unten): Die Oberfläche ist deutsch, und Jarvis begrüßt dich auf Deutsch. Wenn du ihn in einer anderen Sprache ansprichst, antwortet er in dieser Sprache.

Zurück auf Englisch geht so: Öffne `config\api_keys.json` mit dem Editor und ändere `"language": "German"` in `"language": "English"`. Steht die Zeile noch nicht drin, schreib sie direkt hinter die erste geschweifte Klammer `{`, mit einem Komma am Ende: `"language": "English",`.

## Neue Version von mir übernehmen

Wenn ich etwas Neues für dich gebaut habe, bekommst du von mir einen Link zu einem „Pull Request“, also einem Änderungsvorschlag auf GitHub.

1. Öffne den Link und klick auf **„Merge pull request“** und danach auf **„Confirm merge“**.
2. Lade wie in Schritt 3 die neue ZIP herunter und entpacke sie.
3. Kopier aus dem **alten** Ordner diese zwei Dateien an dieselbe Stelle im **neuen** Ordner:
   - `config\api_keys.json` (dein Schlüssel und deine Einstellungen)
   - `memory\long_term.json` (das, was Jarvis sich über dich gemerkt hat)
4. Wenn Jarvis danach eine Fehlermeldung zeigt, führ im neuen Ordner einmal `py -3.12 setup.py` aus.

---

## Jarvis mit Devin verbinden (optional)

Damit kannst du Jarvis sagen, was programmiert werden soll, zum Beispiel:
„Jarvis, sag Devin: Bau mir eine Wetteransage für morgens.“ Jarvis zeigt eine
Rückfrage auf dem Bildschirm. Erst wenn du **BESTÄTIGEN** klickst, startet
Devin. Das verbraucht Devin-Guthaben. Devin baut die Änderung und schickt dir
einen Pull Request, den du wie gewohnt übernimmst.

Einrichten (einmalig):
1. Öffne in Devin **Settings → Devin API → PATs** und erstelle einen Token.
   Kopiere ihn. **Den Token nie weitergeben**, auch nicht im Chat.
2. In Jarvis: **⚙ → PLUGINS → DEVIN** öffnen. Trag den Token und deine
   Organisations-ID ein (beginnt mit `org-`).
3. Klick auf **VERBINDUNG TESTEN**. Erscheint „Verbindung zu Devin steht“,
   ist alles bereit.

Danach kannst du auch fragen: „Jarvis, wie weit ist Devin?“ oder
„Jarvis, sag Devin zusätzlich: Die Ansage soll kürzer sein.“

## Wenn etwas nicht klappt

| Problem | Lösung |
|---|---|
| `py` wird nicht erkannt | Installier Python noch einmal (Schritt 1) und achte auf den Haken bei **„Add python.exe to PATH“**. Öffne danach ein neues schwarzes Fenster. |
| `ModuleNotFoundError: No module named 'xyz'` | Gib `py -3.12 -m pip install xyz` ein, mit dem Namen aus der Fehlermeldung, und starte Jarvis neu. |
| Jarvis hört nichts | Erlaube in Windows unter **Einstellungen → Datenschutz → Mikrofon** den Zugriff für Desktop-Apps. Wähl in Jarvis unter **⚙ → AUDIOGERÄTE** das richtige Mikrofon. |
| Fehlermeldung zum API-Schlüssel | Prüf, ob der Schlüssel vollständig kopiert ist. Wenn nicht, erstell unter https://aistudio.google.com/app/apikey einen neuen. |
| Etwas anderes | Mach ein Foto oder einen Screenshot vom schwarzen Fenster (ohne deinen Schlüssel) und schick ihn mir. |
