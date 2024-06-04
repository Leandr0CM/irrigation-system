from flask import Blueprint, render_template, request
from forms import FormLogin, FormCriarConta
from models.store.users import User


user_ = Blueprint("user", __name__, template_folder='templates')


@user_.route("/")
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)

