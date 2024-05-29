from models.db import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(31), nullable=False, default=str(id + "_irrigation"))
