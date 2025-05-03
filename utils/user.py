from flask import jsonify, Blueprint, request
from utils.jwt_handler import decode_token #type:ignore

user_bp = Blueprint("user", __name__)

@user_bp.route("/me", methods=["GET"])
def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401
    
    token = auth_header.split(" ")[1]
    user_data = decode_token(token)

    if not user_data:
        return jsonify({"error": "Invalid Token"}), 401
    
    return jsonify({
        "username": user_data["username"]
    })

def user_dashboard():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"})
    
    # Fetch metrics