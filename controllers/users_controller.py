from flask import Blueprint, render_template, request
from models.user.users import User
from models.user.roles import Role

user_ = Blueprint("user", __name__, template_folder='templates')

GLOBAL_ROLES = ['Admin', 'Estatístico', 'Operador']

@user_.route("/")
def login():

    for role in GLOBAL_ROLES:
        Role.insert_role(role)

    User.insert_user("Jorge", "1234", GLOBAL_ROLES[0])

    return render_template("login.html")


@user_.route('/check_user', methods=['POST'])
def check_user():
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.get_single_user(name, password)

    return render_template("home.html")


@user_.route("/home")
def home():
    return render_template("home.html")
