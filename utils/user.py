from flask import request
from models.health_metrics import User #type: ignore
from utils.jwt_handler import decode_token #type:ignore
from database.connection import SessionLocal #type: ignore

def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    
    token = auth_header.split(" ")[1]
    user_data = decode_token(token)

    if not user_data:
        return None
    
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_data["user_id"]).first()
    session.close()
    return user