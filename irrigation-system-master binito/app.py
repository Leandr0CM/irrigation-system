from flask import Flask, render_template,request
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#local do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///irrigacao.db'

#criação do banco de dados
database = SQLAlchemy(app)

app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
app.config['MQTT_KEEPALIVE'] = 1500  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

mqtt_client = Mqtt()
mqtt_client.init_app(app)

topic_subscribe = "?" #não iniciado

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/aparelhos")
def aparelhos():
    return render_template("aparelhos.html")

@app.route("/configuracao")
def configuracao():
    return render_template("configuracao.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/gestao")
def gestao():
    return render_template("gestao.html")

if __name__ == "__main__":
    app.run(debug=False)