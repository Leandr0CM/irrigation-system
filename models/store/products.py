from models.db import db
from models.iot.sensors import Sensor
from models.iot.actuators import Actuator


class Product(db.Model):
    __tablename__ = "store"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(31), nullable=False, default=str(id + "_irrigation"))
    is_sold = db.Column('is_sold', db.Boolean, nullable=False, default=False)

    sales = db.relationship("Sale", backref='store', lazy=True, uselist=False)
    devices = db.relationship("Device", backref='store', lazy=True, uselist=False)

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    id_product = db.Column("id_product", db.Integer, db.ForeignKey(Product.id), nullable=False)

    sensors = db.relationship('Sensor', backref='device', lazy=True)
    actuators = db.relationship('Actuator', backref='device', lazy=True)

    def get_all_products():
        products = Product.query.all()
        return products

    def insert_product(name, ultrassonic_sensor, moisture_sensor, pump_water, relay):
        product = Product(name, False)
        device1 = Device(ultrassonic_sensor, False, product.id)
        device2 = Device(moisture_sensor, False, product.id)
        device3 = Device(pump_water, False, product.id)
        device4 = Device(relay, False, product.id)
        actuator1 = Actuator("irrigacao/receber", device1.id)
        actuator2 = Actuator("irrigacao/receber", device2.id)
        sensor1 = Sensor("irrigacao/enviar", device3.id)
        sensor2 = Sensor("irrigacao/enviar", device4.id)

        device1.sensors.append(sensor1)
        device2.sensors.append(sensor2)
        device3.actuators.append(actuator1)
        device4.actuators.append(actuator2)

        product.devices.append(device1)
        product.devices.append(device2)
        product.devices.append(device3)
        product.devices.append(device4)

        db.session.add(product)

        db.session.commit()

        products = Product.query.all()
        return products









