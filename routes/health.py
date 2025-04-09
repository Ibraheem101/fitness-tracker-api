from database.connection import SessionLocal # type: ignore
from models.health_metrics import HealthMetrics # type: ignore
from flask import request, jsonify, Blueprint

health_bp = Blueprint('health', __name__)

@health_bp.route('/metrics', methods=['POST'])
def log_metric():
    data = request.get_json()
    new_metric = HealthMetrics(
        user_id = data['user_id'],
        steps = data['steps'],
        heart_rate = data['heart_rate'],
        calories_burned = data['calories_burned'],
        weight = data['weight'],
        height=data['height']
    )
    session = SessionLocal()
    session.add(new_metric)
    session.commit()

    response = {
            "id": new_metric.id,
            "user_id": new_metric.user_id,
            "steps": new_metric.steps,
            "timestamp": new_metric.timestamp.isoformat()
        }

    session.close()

    return jsonify({
        "message": "Metric logged successfully!",
        "data": response
    }), 201