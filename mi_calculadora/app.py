from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta principal para saber si la calculadora está viva
@app.route('/')
def index():
    return jsonify({
        "status": "online",
        "mensaje": "Bienvenido a la API de la Calculadora",
        "operaciones_disponibles": ["/sumar/a/b", "/restar/a/b"]
    })

# Endpoint para sumar
@app.route('/sumar/<int:a>/<int:b>')
def sumar(a, b):
    resultado = a + b
    return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": resultado})

# Endpoint para restar
@app.route('/restar/<int:a>/<int:b>')
def restar(a, b):
    resultado = a - b
    return jsonify({"operacion": "resta", "a": a, "b": b, "resultado": resultado})

if __name__ == '__main__':
    # Usamos el puerto 5000 que es el estándar de Flask
    app.run(host='0.0.0.0', port=5000)