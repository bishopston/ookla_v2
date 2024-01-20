import csv
from io import StringIO
from psycopg2 import sql, connect
from models import Fixed  # Import your Fixed model

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ookla.settings")

# Configure Django settings
django.setup()

# Sample CSV data (replace with the actual path to your CSV file)
csv_file_path = '/home/alexandros/ookla_speedtests/fixed/aug23/fixed_results_concat_aug23_region.csv'

# Connect to the PostgreSQL database
connection = connect(
    dbname='ookla',
    user='ookla_user',
    password='!@#ooklauser1',
    host='localhost',
    port='5432',
)

cursor = connection.cursor()

# Read CSV file and insert into the Fixed table
try:
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            country, area, service, provider_name, provider_id, period, p25_download_mbps, p75_download_mbps = row

            # Create a Fixed object and save it to the database
            Fixed.objects.create(
                country=country,
                area=area,
                service=service,
                provider_name=provider_name,
                provider_id=int(provider_id),
                period=period,
                p25_download_mbps=float(p25_download_mbps),
                p75_download_mbps=float(p75_download_mbps),
            )

    # Commit the changes to the database
    connection.commit()

except Exception as e:
    print(f"Error: {e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
