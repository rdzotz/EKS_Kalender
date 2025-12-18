import csv
import os
import hashlib
from datetime import datetime
from ics import Calendar, Event
from dateutil import parser
import sys

def generate_uid(subject, start_date):
    """Generate a stable UID based on the event subject and start date."""
    hash_input = f"{subject}-{start_date}".encode('utf-8')
    return hashlib.sha1(hash_input).hexdigest() + "@eks-kalender.de"

def main():
    csv_file = "calendar.csv"
    output_dir = "web"
    output_file = os.path.join(output_dir, "school-calendar.ics")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        sys.exit(1)

    cal = Calendar()

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                e = Event()
                e.name = row['Subject']
                
                start_str = row['Start Date']
                end_str = row['End Date']
                all_day = row['All Day'].upper() == 'TRUE'
                
                start_dt = parser.parse(start_str)
                end_dt = parser.parse(end_str)

                if all_day:
                    e.begin = start_dt.date()
                    # For all-day events in ICS, end date is non-inclusive, 
                    # so if it ends on 2026-01-05, we set end to 2026-01-06
                    from datetime import timedelta
                    e.make_all_day()
                    e.end = end_dt.date() + timedelta(days=1)
                else:
                    e.begin = start_dt
                    e.end = end_dt

                e.description = row.get('Description', '')
                e.location = row.get('Location', '')
                e.uid = generate_uid(e.name, start_str)
                
                cal.events.add(e)
            except Exception as ex:
                print(f"Skipping row due to error: {row}. Error: {ex}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cal.serialize_iter())
    
    print(f"Successfully generated {output_file} with {len(cal.events)} events.")

if __name__ == "__main__":
    main()

