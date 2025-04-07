from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
class HealthMetrics(Base):
    __tablename__ = "health_metrics"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    steps = Column(Integer)
    heart_rate = Column(Integer)
    calories = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)