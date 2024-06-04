from flask import Blueprint, render_template, request
from models.store.products import Product


product_ = Blueprint("store", __name__, template_folder='templates')

@product_.route("/produtos")
def produtos():
    products = Product.get_all_products()
    return render_template("produtos.html", products=products)

@product_.route("/registrar_produto")
def registrar_produto():
    return render_template("registrar_produto.html")

@product_.route("/adicionar_produto", methods=['POST'])
def registrar_produto():
    name = request.form.get("name")
    ultrassonic_sensor = request.form.get("ultrassonic_sensor")
    moisture_sensor = request.form.get("moisture_sensor")
    pump_water = request.form.get("pump_water")
    relay = request.form.get("relay")

    Product.insert_product(name, ultrassonic_sensor, moisture_sensor, pump_water, relay)
    products = Product.get_all_products()

    return render_template("registrar_produto.html", products=products)