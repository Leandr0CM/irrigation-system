from flask import Flask, render_template
from models.db import db, instance
from flask_mqtt import Mqtt


def create_app():
    app = Flask(__name__,
                root_path="./",  # raiz de path
                template_folder="./templates/", #deve estar no root por padrão
                )

    #configura o banco de dados
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    #app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    #app.config['MQTT_BROKER_PORT'] = 1883
    #app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    #app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    #app.config['MQTT_KEEPALIVE'] = 1500  # Set KeepAlive time in seconds
    #app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    #mqtt_client = Mqtt()
    #mqtt_client.init_app(app)

    topic_subscribe = "?" #não iniciado

    @app.route("/")
    def login():
        return render_template("login.html")


    return app