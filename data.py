import csv
from models import db, Data

def populate_database_from_csv():
    with open('utils/raw_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            device_fk_id = int(row['device_fk_id'])
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            time_stamp = row['time_stamp']
            sts = True if row['sts'] == '1' else False
            speed = float(row['speed'])
            data = Data(device_fk_id, latitude, longitude, time_stamp, sts, speed)
            db.session.add(data)
    db.session.commit()
