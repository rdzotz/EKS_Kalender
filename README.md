# School Calendar Automation

This project automates the generation of a school calendar ICS file from a CSV source of truth.

## Usage

1. Edit `calendar.csv`.
2. Push to GitHub.
3. GitHub Actions will regenerate `web/school-calendar.ics` and update the website.

## Local Development

Using `uv`:
```bash
uv run generate_ics.py
```

