import os
import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set")

def create_token(data: dict, expires_in: int = 60):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_in)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256") #type:ignore

def decode_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"]) #type: ignore
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None