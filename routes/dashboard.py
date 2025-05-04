from flask import jsonify, Blueprint
from models.health_metrics import HealthMetrics #type: ignore
from utils.user import get_current_user #type: ignore
from database.connection import SessionLocal #type:ignore

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def user_dashboard():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401
    
    session = SessionLocal()
    metrics = session.query(HealthMetrics).filter_by(user_id=user.id).all()
    session.close()
    
    # Fetch metrics
    return jsonify({"username": user.username})
