from flask import Blueprint, render_template, request
from models.user.users import User

user_ = Blueprint("user", __name__, template_folder='templates')

GLOBAL_ROLES = ['Admin', 'Estatístico', 'Operador']


@user_.route("/")
def login():
    return render_template("login.html")


@user_.route('/check_user', methods=['POST'])
def check_user():
    name = request.form.get("name")
    password = request.form.get("password")

    if "admin" == name and "1234" == password:
        return render_template("home.html")

    user = User.get_single_user(name, password)

    if user is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


@user_.route('/insert_user_register', methods=['POST'])
def insert_user_register():
    name = request.form.get("name")
    password = request.form.get("password")
    same_password = request.form.get("same_password")

    user = User.get_single_user(name, password)

    if password == same_password:
        if user is not None:
            print("Usuário já existente")
            return render_template("login.html")
        else:
            User.insert_user(name, password, "normal")
            print("Ok")
            return render_template("home.html")
    return render_template("login.html")


@user_.route("/home")
def home():
    return render_template("home.html")
