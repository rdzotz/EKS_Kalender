# School Calendar Automation

This project automates the generation of a school calendar ICS file from a CSV source of truth.

## Usage

1. Edit `calendar.csv`.
2. Push to GitHub.
3. GitHub Actions will regenerate `web/school-calendar.ics` and update the website.

## Disclaimer & Contributions

**Haftungsausschluss**: Dies ist ein **privates Projekt** und steht in **keiner offiziellen Verbindung** zur Erich Kästner Grundschule. Der Kalender wird privat betrieben und automatisiert erstellt. Wir übernehmen keine Gewähr für die Richtigkeit der Daten. Maßgeblich sind die offiziellen Mitteilungen der Schule.

**Mithilfe erwünscht**: Wenn Sie Fehler finden oder Termine fehlen, erstellen Sie bitte einen **Pull Request** für die `calendar.csv` oder eröffnen Sie ein **Issue**.

## Local Development

Using `uv`:
```bash
uv run generate_ics.py
```

