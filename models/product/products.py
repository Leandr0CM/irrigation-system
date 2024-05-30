from models.db import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(31), nullable=False, default=str(id + "_irrigation"))
    is_saled = db.Column('is_saled', db.Boolean, nullable=False, default=False)
    sales = db.relationship("Device", backref='role', lazy=True, uselist=False)
