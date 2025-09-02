from sqlalchemy import Column, Integer, String, Boolean, Float, Date, DateTime
from sqlalchemy.sql import func
from database import Base # <-- FIX: Removed the dot from .database

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # --- Recommended Additions ---
    full_name = Column(String)
    date_of_birth = Column(Date)
    sex_assigned_at_birth = Column(String)
    primary_health_goal = Column(String)
    
    # --- Onboarding Data from Figma ---
    # Physical
    exercise_hours_yesterday = Column(Float)
    sleep_hours_last_night = Column(Float)
    had_sleep_disturbances = Column(Boolean)
    feels_thirsty_at_night = Column(Boolean)
    
    # Emotional
    overall_mood_rating = Column(Integer)
    stress_level = Column(String)
    
    # Cognitive
    focus_rating = Column(Integer)
    forgets_things_often = Column(Boolean)
    brain_fog_severity = Column(Integer)
    
    # Energy
    current_energy_rating = Column(Integer)
    most_energized_time = Column(String)
