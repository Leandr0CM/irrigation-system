from models.db import db
from models.user.roles import Role

#https://www.youtube.com/watch?v=7AkJvQXOjYg

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(255), nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    id_role = db.Column("role", db.Integer, db.ForeignKey(Role.id), nullable=False)

    def get_single_user(name, password):
        user = User.query.filter(User.name == name and User.password == password).first()
        return user

    def get_all_users():
        users = User.query.with_entities(User.name, User.password, User.id_role).all()
        return users

    def insert_user(name, password, identifier):
        role = Role.query.filter_by(identifier=identifier).first()
        user = User(name=name, password=password, id_role=role.id)

        db.session.add(user)
        db.session.commit()

