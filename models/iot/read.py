from models.db import db
from models.iot.sensors import Sensor
from models.iot.devices import Device
from datetime import datetime

class Read(db.Model):
    __tablename__ = 'read'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    read_datetime = db.Column(db.DateTime(), nullable=False)
    sensors_id = db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable=False)
    value = db.Column(db.Float, nullable=True)