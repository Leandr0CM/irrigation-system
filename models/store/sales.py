from models.db import db
from models.store.users import User
from models.store.products import Product


class Sale(db.Model):
    __tablename__ = "sale"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey(User.id), nullable=False)
    id_product = db.Column("id_product", db.Integer, db.ForeignKey(Product.id), nullable=False)
