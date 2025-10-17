from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Ruta raíz para comprobar que el servidor está vivo
@app.route("/", methods=["GET"])
def root():
    return jsonify({"ok": True, "message": "Backend Flask levantado. Usa /action para GET/POST."})

# /action acepta GET y POST
@app.route("/action", methods=["GET", "POST"])
def action():
    if request.method == "GET":
        return jsonify({"ok": True, "message": "GET recibido en /action"})
    # POST
    data = request.get_json(silent=True) or {}
    return jsonify({"ok": True, "message": "POST recibido en /action", "received": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
