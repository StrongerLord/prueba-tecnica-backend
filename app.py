from flask import Flask
from routes.tasks import tasks_blueprint
from routes.auth import auth_blueprint
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI, JWT_SECRET_KEY
from utils.db import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app, origins=["https://prueba-tecnica.memz.live", "http://localhost:5173"])

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

jwt = JWTManager(app)
app.register_blueprint(tasks_blueprint)
app.register_blueprint(auth_blueprint)

db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)