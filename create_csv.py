import csv

data = [
    ["Projekttag Weihnachten", "2025-12-19 08:00", "2025-12-19 11:30", "FALSE", "Projekttag Weihnachten", ""],
    ["2. Schulversammlung - Weihnachtssingen", "2025-12-19 08:50", "2025-12-19 09:35", "FALSE", "2. Schulversammlung - Weihnachtssingen", ""],
    ["Weihnachtsferien", "2025-12-20", "2026-01-05", "TRUE", "Hort geschlossen!", ""],
    ["1. Schultag nach den Weihnachtsferien", "2026-01-05", "2026-01-05", "TRUE", "", ""],
    ["4. ESL", "2026-01-07 13:45", "2026-01-07 15:00", "FALSE", "", ""],
    ["Hockeyturnier, Klasse 3+4", "2026-01-14", "2026-01-14", "TRUE", "", ""],
    ["2-Felder-Ball-Turnier, Klasse 3+4", "2026-01-15 08:50", "2026-01-15 12:40", "FALSE", "2. - 5. Stunde", ""],
    ["Elternabend „Nein-Tonne“ für Klasse 1 + 2", "2026-01-22 18:00", "2026-01-22 19:30", "FALSE", "", ""],
    ["Theater: „Nein-Tonne“ Klasse 1 und 2", "2026-01-27 08:50", "2026-01-27 11:30", "FALSE", "2. – 4. Stunde", ""],
    ["Zeugnisausgabe", "2026-01-30 09:55", "2026-01-30 10:40", "FALSE", "Unterrichtsende nach der 3. Stunde", ""],
    ["Winterferien", "2026-01-31", "2026-02-09", "TRUE", "", ""],
    ["1. Schultag nach den Winterferien", "2026-02-09", "2026-02-09", "TRUE", "", ""],
    ["2. Präventionsteam", "2026-02-11 15:00", "2026-02-11 16:30", "FALSE", "", ""],
    ["Fasching", "2026-02-16", "2026-02-16", "TRUE", "", ""],
    ["5. ESL und 2. Steuergruppe", "2026-02-18 13:45", "2026-02-18 15:00", "FALSE", "", ""],
    ["Schulfestvorbereitungsgruppe", "2026-02-18 15:00", "2026-02-18 16:00", "FALSE", "", ""],
    ["5. KSK", "2026-02-25 13:45", "2026-02-25 15:00", "FALSE", "", ""],
    ["3. Gesamtkonferenz (GK)", "2026-03-04 16:30", "2026-03-04 18:30", "FALSE", "", ""],
    ["3. Gesamtschülervertretung (GSV)", "2026-03-06 10:45", "2026-03-06 11:30", "FALSE", "", ""],
    ["3. Gesamtelternvertretung (GEV)", "2026-03-10 19:00", "2026-03-10 21:00", "FALSE", "", ""],
    ["3. Schulkonferenz (SK)", "2026-03-11 16:30", "2026-03-11 18:00", "FALSE", "", ""],
    ["Känguru-Wettbewerb für 3.-6. Klassen", "2026-03-19 09:55", "2026-03-19 11:30", "FALSE", "", ""],
    ["Projektwoche Umwelt- und Mobilitätserziehung", "2026-03-23", "2026-03-28", "TRUE", "", ""],
    ["Tag der offenen Tür", "2026-03-27 09:30", "2026-03-27 11:00", "FALSE", "", ""],
    ["Osterferien", "2026-03-28", "2026-04-13", "TRUE", "", ""],
    ["1. Schultag nach den Osterferien", "2026-04-13", "2026-04-13", "TRUE", "", ""],
    ["Elternabend „Mein Körper gehört mir“ für Klasse 3+4", "2026-04-14 18:00", "2026-04-14 20:00", "FALSE", "", ""],
    ["Theater: Mein Körper gehört mir Teil 1 (Kl 4)", "2026-04-15 08:50", "2026-04-15 12:40", "FALSE", "2. – 5. Stunde", ""],
    ["Feedbackgespräche", "2026-04-17", "2026-04-17", "TRUE", "Angeleitetes Lernen zu Hause", ""],
    ["Feedbackgespräche", "2026-04-20", "2026-04-20", "TRUE", "Angeleitetes Lernen zu Hause", ""],
    ["Theater: Mein Körper … Teil 2 (Kl 4)", "2026-04-22 08:50", "2026-04-22 12:40", "FALSE", "2. – 5. Stunde", ""],
    ["Theater: Mein Körper … Teil 1 (Kl 3)", "2026-04-24 08:50", "2026-04-24 11:30", "FALSE", "2. – 4. Stunde", ""],
    ["Theater: Mein Körper … Teil 3 (Kl 4)", "2026-04-29 08:50", "2026-04-29 12:40", "FALSE", "2. – 5. Stunde", ""],
    ["6. ESL", "2026-04-29 13:45", "2026-04-29 15:00", "FALSE", "", ""],
    ["Tag der Arbeit", "2026-05-01", "2026-05-01", "TRUE", "Feiertag", ""],
    ["6. KSK", "2026-05-06 13:45", "2026-05-06 15:00", "FALSE", "", ""],
    ["Theater: Mein Körper … Teil 2 (Kl 3)", "2026-05-08 08:50", "2026-05-08 11:30", "FALSE", "2. – 4. Stunde", ""],
    ["Himmelfahrt & Brückentag", "2026-05-14", "2026-05-16", "TRUE", "Hort geschlossen!", ""],
    ["Theater: Mein Körper … Teil 3 (Kl 3)", "2026-05-18 08:50", "2026-05-18 11:30", "FALSE", "2. – 4. Stunde", ""],
    ["4. Gesamtelternvertretung (GEV)", "2026-05-19 19:00", "2026-05-19 21:00", "FALSE", "", ""],
    ["Schnupperstunde für zukünftige Schulanfänger", "2026-05-20 12:00", "2026-05-20 16:30", "FALSE", "", ""],
    ["4. Gesamtschülervertretung (GSV)", "2026-05-22 09:55", "2026-05-22 10:40", "FALSE", "", ""],
    ["Pfingstmontag & schulfreier Tag", "2026-05-25", "2026-05-27", "TRUE", "Hort geschlossen!", ""],
    ["4. Gesamtkonferenz (GK)", "2026-05-27 16:30", "2026-05-27 18:30", "FALSE", "", ""],
    ["Bundesjugendspiele Klasse 1+2", "2026-05-28", "2026-05-28", "TRUE", "", ""],
    ["Schulfest", "2026-05-29 15:00", "2026-05-29 18:00", "FALSE", "", ""],
    ["4. Schulkonferenz (SK)", "2026-06-10 16:30", "2026-06-10 18:00", "FALSE", "", ""],
    ["0. Elternabend für Schulanfänger", "2026-06-17 17:00", "2026-06-17 19:00", "FALSE", "", ""],
    ["4. Schulversammlung / Verabschiedungsfeier", "2026-07-08 08:50", "2026-07-08 09:35", "FALSE", "", ""],
    ["Zeugnisausgabe (3. Stunde)", "2026-07-08 09:55", "2026-07-08 10:40", "FALSE", "", ""],
    ["Letzter Schultag", "2026-07-08", "2026-07-08", "TRUE", "Unterrichtsende nach der 3. Stunde", ""],
    ["Sommerferien", "2026-07-09", "2026-08-24", "TRUE", "", ""],
    ["1. Schultag nach den Ferien", "2026-08-24", "2026-08-24", "TRUE", "", ""]
]

header = ["Subject", "Start Date", "End Date", "All Day", "Description", "Location"]

with open("calendar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

