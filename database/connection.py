import os
import time
import psycopg2
from dotenv import load_dotenv

url = os.getenv("DATABASE_URL")
while True:
    try:
        connection = psycopg2.connect(url)
        print("DB ready")
        break
    except psycopg2.OperationalError:
        print("DB not ready. Retrying ...")
        time.sleep(5)