from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    device_fk_id = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    sts = db.Column(db.Boolean)
    speed = db.Column(db.Float)

    def __init__(self, device_fk_id, latitude, longitude, time_stamp, sts, speed):
        self.device_fk_id = device_fk_id
        self.latitude = latitude
        self.longitude = longitude
        self.time_stamp = datetime.strptime(time_stamp, '%Y-%m-%dT%H:%M:%SZ')
        self.sts = sts
        self.speed = speed
