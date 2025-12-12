from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "clave_secreta_para_el_carrito"

# -----------------------
#  UTIL / CARGA DE DATOS
# -----------------------
def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_orders():
    if not os.path.exists("orders.json"):
        with open("orders.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
    with open("orders.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_order(order):
    orders = load_orders()
    orders.append(order)
    with open("orders.json", "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4, ensure_ascii=False)

# ------------------------
#        RUTAS
# ------------------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/catalogo")
def catalogo():
    productos = load_products()
    return render_template("products.html", productos=productos)

@app.route("/producto/<int:id>")
def product_detail(id):
    productos = load_products()
    producto = next((p for p in productos if p["id"] == id), None)
    return render_template("product_detail.html", producto=producto)

@app.route("/agregar/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(id)
    session.modified = True
    return redirect(url_for("cart"))

# ------------------------
# Carrito modificado con cantidad y subtotal
# ------------------------
@app.route("/carrito")
def cart():
    productos = load_products()
    carrito_ids = session.get("cart", [])

    # Contar cantidad de cada producto
    carrito_count = {}
    for pid in carrito_ids:
        carrito_count[pid] = carrito_count.get(pid, 0) + 1

    # Construir lista de productos con cantidad y subtotal
    carrito_detalle = []
    for pid, cantidad in carrito_count.items():
        producto = next((p for p in productos if p["id"] == pid), None)
        if producto:
            carrito_detalle.append({
                "id": producto["id"],
                "nombre": producto["nombre"],
                "precio": producto.get("precio", 0),
                "cantidad": cantidad,
                "subtotal": producto.get("precio", 0) * cantidad,
                "imagen": producto.get("imagen", "")
            })

    return render_template("cart.html", carrito=carrito_detalle)

# ------------------------
# Confirmar pedido
# ------------------------
@app.route("/confirmar")
def confirm():
    productos = load_products()
    carrito_ids = session.get("cart", [])

    # Contar cantidad y crear items
    carrito_count = {}
    for pid in carrito_ids:
        carrito_count[pid] = carrito_count.get(pid, 0) + 1

    items = []
    total = 0
    for pid, cantidad in carrito_count.items():
        producto = next((p for p in productos if p["id"] == pid), None)
        if producto:
            subtotal = producto.get("precio", 0) * cantidad
            total += subtotal
            items.append({
                "id": producto["id"],
                "nombre": producto["nombre"],
                "precio_unitario": producto.get("precio", 0),
                "cantidad": cantidad,
                "subtotal": subtotal
            })

    # Generar order_id
    orders = load_orders()
    order_id = (max((o.get("order_id", 0) for o in orders), default=0) + 1)

    order = {
        "order_id": order_id,
        "items": items,
        "total": total,
        "estado": "Pendiente",
        "fecha": datetime.utcnow().isoformat() + "Z"
    }

    save_order(order)
    session["cart"] = []
    session.modified = True

    return render_template("confirm.html", order=order)

@app.route("/pedidos")
def pedidos():
    orders = load_orders()
    return render_template("pedidos.html", pedidos=orders)

# ------------------------
# Ruta temporal JSON
# ------------------------
@app.route("/ver_pedido")
def ver_pedido():
    productos = load_products()
    carrito_ids = session.get("cart", [])

    if not carrito_ids:
        return jsonify({"mensaje": "El carrito está vacío"})

    carrito_count = {}
    for pid in carrito_ids:
        carrito_count[pid] = carrito_count.get(pid, 0) + 1

    carrito_detalle = []
    total_general = 0
    for pid, cantidad in carrito_count.items():
        producto = next((p for p in productos if p["id"] == pid), None)
        if producto:
            subtotal = producto.get("precio", 0) * cantidad
            total_general += subtotal
            carrito_detalle.append({
                "id": producto["id"],
                "nombre": producto["nombre"],
                "precio_unitario": producto.get("precio", 0),
                "cantidad": cantidad,
                "subtotal": subtotal
            })

    return jsonify({
        "items": carrito_detalle,
        "total": total_general
    })

# Ejecutar app
if __name__ == "__main__":
    app.run(debug=True)
