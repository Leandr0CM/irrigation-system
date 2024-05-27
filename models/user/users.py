from models import db

#https://www.youtube.com/watch?v=7AkJvQXOjYg

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)