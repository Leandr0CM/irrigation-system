from models.db import db
from models.product.products import Product

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    id_product = db.Column("id_product", db.Integer, db.ForeignKey(Product.id), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)

    sensors = db.relationship('Sensor', backref='devices', lazy=True)
    actuators = db.relationship('Actuator', backref='devices', lazy=True)