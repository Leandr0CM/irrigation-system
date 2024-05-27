#local de armazenamento de banco de dados
from datetime import datetime
#from app import database

#entidades
#lazy: mostra todos os atributos do autor de forma direta
#default: quando o cliente não realizou nenhuma compra

#usuário
class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    compras = database.relationship('Compra', nullable=False, backref='comprador', lazy=True, default='Sem compras no momento')


#administrador
class Admin(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)


#compra - produto e usuário
class Compra(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    id_produto = database.Column(database.Integer, database.ForeignKey('produto.id'), nullable=False)
    data_compra = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


class Produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False, default=f"{id}_produto")
    compra = database.relationship('Compra', backref='produto', lazy=True)
    atuador = database.relationship('Atuador', backref='atuador', lazy=True)
    sensor = database.relationship('Sensor', backref='sensor', lazy=True)


#atuador - produto
class Atuador(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False, default=f"{id}_atuador")
    id_produto = database.Column(database.Integer, database.ForeignKey('produto.id'), nullable=False)
    id_tipo_atuador = database.Column(database.Integer, database.ForeignKey('tipoatuador.id'), nullable=False)


#sensor - produto
class Sensor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_produto = database.Column(database.Integer, database.ForeignKey('produto.id'), nullable=False)
    id_tipo_sensor = database.Column(database.Integer, database.ForeignKey('tiposensor.id'), nullable=False)

#tipo de atuador
class TipoAtuador(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False, default=f"{id}_atuador")


#tipo de sensor
class TipoSensor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False, default=f"{id}_sensor")

#dado do sensor
class DadoSensor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    valor = database.Column(database.Integer)
    data_hora = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
