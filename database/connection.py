import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.health_metrics import Base #type:ignore

load_dotenv()
url = os.getenv("DATABASE_URL")
if not url:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

# Create tables (Not for prod)
# Base.metadata.create_all(bind=engine)
print("Tables created successfully.")