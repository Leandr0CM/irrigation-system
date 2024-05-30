from models.db import db

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column("identifier", db.String(20), nullable=False, unique=True)

    #vários usuários associados a uma role (tabela, atributo, todas as informações)
    users = db.relationship("User", backref='role', lazy=True)

    #usado apenas uma vez
    def insert_role(identifier):
        role = Role(identifier=identifier)
        db.session.add(role)
        db.session.commit()