from models import db

class UserRole(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    identifier = db.Column(db.String(10), nullable=False, unique=True)

    #vários usuários associados a uma role (tabela, atributo, todas as informações)
    users =  db.relationship("User", backref='role', lazy=True)