import os
import time
import psycopg2
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

url = os.getenv("DATABASE_URL")
while True:
    try:
        connection = psycopg2.connect(url)
        print("DB ready")
        break
    except psycopg2.OperationalError:
        print("DB not ready. Retrying ...")
        time.sleep(5)

@app.get('/')
def test():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
