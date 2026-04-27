from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Aplicación CI/CD funcionando 🚀</h1>"

print("Archivo app.py cargado correctamente")

if __name__ == "__main__":
    print("Iniciando servidor Flask en puerto 8080...")
    app.run(host="0.0.0.0", port=8080)