from datetime import datetime, timezone
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    health_metrics = relationship("HealthMetrics", backref="user", cascade="all, delete")
    
class HealthMetrics(Base):
    __tablename__ = "health_metrics"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    steps = Column(Integer)
    heart_rate = Column(Integer)
    calories_burned = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))