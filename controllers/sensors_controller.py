from flask import Blueprint, render_template, request
from models.iot.sensors import Sensor


sensor_ = Blueprint("sensor", __name__, template_folder='templates')

@sensor_.route("/sensores")
def sensores():
    return render_template("sensores.html")