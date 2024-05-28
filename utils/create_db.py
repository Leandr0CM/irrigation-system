from flask import Flask
from models.user.roles import Role
from models import *

#trata-se de um módulo reutilizável (utilities)
def create_db(app: Flask):
    with app.app_context():
        db.drop_all() #elimina o banco de dados
        db.create_all() #cria um novo a partir de dados novos

        GLOBAL_IDENTIFIERS = ['admnistrador', "estatístico", "operador", "normal"]

        for identifier in GLOBAL_IDENTIFIERS:
            Role.insert_role(identifier)

