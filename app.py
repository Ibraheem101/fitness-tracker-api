from flask import Flask
from routes.health import health_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(health_bp, url_prefix="/api")

@app.get('/')
def test():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
