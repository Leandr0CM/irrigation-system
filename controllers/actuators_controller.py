from flask import Blueprint, render_template, request
from models.iot.sensors import Sensor


actuator_ = Blueprint("actuator", __name__, template_folder='templates')

@actuator_.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html")