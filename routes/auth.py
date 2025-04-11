from flask import Blueprint, request, jsonify
from models.models import User
from utils.db import db
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    request_data = request.get_json() if request.is_json else request.form.to_dict()
    username = request_data.get('username', '')
    password = request_data.get('password', '')
    user = User.query.filter_by(username=username).first()

    if not request_data or not username or not password:
        return jsonify({'message': 'Missing fields in request'}), 400
    if not user:
        return jsonify({'message': 'User not found'}), 404
    if user.password != password:
        return jsonify({'message': 'Invalid password'}), 401
    if user and user.password == password:
        access_token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=30))
        return jsonify({'message': 'Login successful', 'token': access_token}), 200
    else:
        return jsonify({'message': 'Something went wrong on the server'}), 500

