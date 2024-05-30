from flask import Flask
from models.db import db, instance
from controllers.users_controller import user_
from controllers.sensors_controller import sensor_
from controllers.actuators_controller import actuator_


from flask_mqtt import Mqtt


def create_app():
    app = Flask(__name__,
                root_path="./",  # raiz de path
                template_folder="./templates/",  # deve estar no root por padrão
                )

    app.register_blueprint(user_, url_prefix='/')
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')


    # configura o banco de dados
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance


    db.init_app(app)

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 1500  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    # mqtt_client = Mqtt()
    # mqtt_client.init_app(app)

    topic_subscribe = "?"  # não iniciado

    return app
