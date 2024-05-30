from models.db import db
from models.iot.actuators import Actuator
from models.iot.devices import Device
from datetime import datetime

class Write(db.Model):
    __tablename__ = 'write'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    write_datetime = db.Column(db.DateTime(), nullable=False)
    actuators_id = db.Column(db.Integer, db.ForeignKey(Actuator.id), nullable=False)
    value = db.Column(db.Float, nullable=True)