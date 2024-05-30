from models.db import db
from models.user.users import User
from models.product.products import Product

#https://www.youtube.com/watch?v=7AkJvQXOjYg

class Sales(db.Model):
    __tablename__ = "sales"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey(User.id), nullable=False)
    id_product = db.Column("id_product", db.Integer, db.ForeignKey(Product.id), nullable=False)
