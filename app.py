from flask import Flask
from routes.tasks import tasks_blueprint
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI
from utils.db import db
import os

app = Flask(__name__)
CORS(app, origins=["https://prueba-tecnica.memz.live", "http://localhost:5173"])

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(tasks_blueprint)

db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)