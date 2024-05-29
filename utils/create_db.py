from flask import Flask
from models.user.roles import Role
from models.user.users import User
from models import *

#trata-se de um módulo reutilizável (utilities)
def create_db(app: Flask):
    with app.app_context():
        db.drop_all() #elimina o banco de dados
        db.create_all() #cria um novo a partir de dados novos

        GLOBAL_IDENTIFIERS = ["administrador", "estatístico", "operador", "normal"]
        PRIMARY_USERS = {
            "Jorge": ["1234", GLOBAL_IDENTIFIERS[0]],
            "Leandro": ["1234", GLOBAL_IDENTIFIERS[1]],
            "Joelton": ["1234", GLOBAL_IDENTIFIERS[2]]
        }

        for identifier in GLOBAL_IDENTIFIERS:
            Role.insert_role(identifier)

        for key, value in PRIMARY_USERS.items():
            print(PRIMARY_USERS[key])
            User.insert_user(key, PRIMARY_USERS[key][0], PRIMARY_USERS[key][1])

        users = User.get_all_users()
        print(users)

