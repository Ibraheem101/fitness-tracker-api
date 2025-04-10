from flask import jsonify, Blueprint, request
from models.health_metrics import User #type:ignore
from utils.security import verify_password #type:ignore
from utils.jwt_handler import create_token #type:ignore
from database.connection import SessionLocal #type:ignore

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    session = SessionLocal()
    user = session.query(User).filter_by(username=username).first()

    if not user or not verify_password(password, user.password_hash):
        session.close()
        return jsonify({"error": "Invalid Credentials"}), 401
    token = create_token({"user_id": user.id})
    session.close()
    return jsonify({"token": token}), 200