from flask import Flask, render_template, jsonify
from game.juego import Juego

app = Flask(__name__)
juego = Juego()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/estado")
def estado():
    return jsonify(juego.estado())

@app.route("/iniciar")
def iniciar():
    return jsonify(juego.iniciar())

@app.route("/atacar")
def atacar():
    return jsonify(juego.atacar())

@app.route("/interactuar")
def interactuar():
    return jsonify(juego.interactuar())

@app.route("/huir")
def huir():
    return jsonify(juego.huir())

@app.route("/powerup")
def powerup():
    return jsonify(juego.powerup())

if __name__ == "__main__":
    app.run(debug=True)
