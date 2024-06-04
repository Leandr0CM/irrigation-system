from flask import Flask
from models import db
from models.store.users import User


def create_db(app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()

        #root users
        root_users = {
            "Jorge": ["jorge@gmail.com", "12", "administrador"],
            "Leandro": ["leandro@gmail.com", "123", "estatístico"],
            "Joelton": ["joelton@gmail.com", "1234", "normal"]
        }

        for key, value in root_users.items():
            User.insert_user(key, root_users[key][0], root_users[key][1])
