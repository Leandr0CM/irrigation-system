from models.db import db
from models.iot.devices import Device

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', db.Integer, primary_key = True)
    devices_id = db.Column(db.Integer, db.ForeignKey(Device.id))
    topic = db.Column(db.String(50))