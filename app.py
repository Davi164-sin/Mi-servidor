from flask import Flask, render_template, request, jsonify
# Importamos las herramientas que ya programaste en tu archivo
from asistente_pc import obtener_clima, generar_contrasena, convertir_unidades, enviar_telegram

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>🚀 Panel de Control de mi Asistente SaaS</h1>
    <p>El servidor está en línea en la nube.</p>
    """

# API para que tu frontend HTML consulte el clima de un cliente
@app.route("/api/clima", methods=["GET"])
def api_clima():
    ciudad = request.args.get("ciudad", "Bogota")
    res = obtener_clima(ciudad)
    return jsonify({"resultado": res})

# API para generar contraseñas desde la web
@app.route("/api/password", methods=["GET"])
def api_password():
    longitud = int(request.args.get("longitud", 16))
    pwds = generar_contrasena(longitud, cantidad=1)
    return jsonify({"contrasena": pwds[0]})

# API para mandar alertas automáticas a tu cliente por Telegram
@app.route("/api/alerta", methods=["POST"])
def api_alerta():
    datos = request.get_json()
    msg = datos.get("mensaje", "Alerta del sistema")
    res = enviar_telegram(msg)
    return jsonify({"status": res})

if __name__ == "__main__":
    app.run(debug=True)
