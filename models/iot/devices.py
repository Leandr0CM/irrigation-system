from models.db import db
from models.store.products import Product

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    id_product = db.Column("id_product", db.Integer, db.ForeignKey(Product.id), nullable=False)

    sensors = db.relationship('Sensor', backref='device', lazy=True)
    actuators = db.relationship('Actuator', backref='device', lazy=True)