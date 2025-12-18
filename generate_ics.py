import csv
import os
import hashlib
from datetime import datetime, timedelta
from ics import Calendar, Event
from dateutil import parser
import sys

def generate_uid(subject, start_date, year_folder):
    """Generate a stable UID based on the event subject, start date, and academic year."""
    hash_input = f"{year_folder}-{subject}-{start_date}".encode('utf-8')
    return hashlib.sha1(hash_input).hexdigest() + "@eks-kalender.de"

def process_calendar(csv_path, output_path, year_folder):
    if not os.path.exists(csv_path):
        print(f"Skipping: {csv_path} (not found)")
        return

    cal = Calendar()
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
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
                    e.make_all_day()
                    # Exclusive end date for all-day events
                    e.end = end_dt.date() + timedelta(days=1)
                else:
                    e.begin = start_dt
                    e.end = end_dt

                e.description = row.get('Description', '')
                e.location = row.get('Location', '')
                e.uid = generate_uid(e.name, start_str, year_folder)
                
                cal.events.add(e)
            except Exception as ex:
                print(f"Skipping row in {csv_path} due to error: {row}. Error: {ex}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(cal.serialize_iter())
    
    print(f"Successfully generated {output_path} with {len(cal.events)} events.")

def main():
    data_dir = "data"
    web_dir = "web/calendars"
    
    if not os.path.exists(web_dir):
        os.makedirs(web_dir)

    # Process all year folders in data/
    if not os.path.exists(data_dir):
        print(f"Error: {data_dir} directory not found.")
        sys.exit(1)

    for year_folder in os.listdir(data_dir):
        year_path = os.path.join(data_dir, year_folder)
        if os.path.isdir(year_path):
            csv_file = os.path.join(year_path, "calendar.csv")
            output_file = os.path.join(web_dir, f"eks_{year_folder}.ics")
            process_calendar(csv_file, output_file, year_folder)

if __name__ == "__main__":
    main()
