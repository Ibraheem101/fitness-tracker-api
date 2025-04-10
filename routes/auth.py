from flask import jsonify, Blueprint, request
from models.health_metrics import User #type:ignore
from utils.security import hash_password #type:ignore
from database.connection import SessionLocal #type:ignore

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/create-test-user', methods=['POST'])

def create_user():
    data = request.get_json()
    user = User(
        username = data['username'],
        email = data['email'],
        password_hash = hash_password(data['password_hash'])
    )
    session = SessionLocal()
    session.add(user)
    session.commit()
    session.close()

    return {"message": "User Created"}, 201