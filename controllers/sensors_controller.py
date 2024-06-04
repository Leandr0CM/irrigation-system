from flask import Blueprint, render_template, request


sensor_ = Blueprint("sensor", __name__, template_folder='templates')

@sensor_.route("/sensores")
def sensores():
    return render_template("sensores.html")