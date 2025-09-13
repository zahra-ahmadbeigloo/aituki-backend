from sqlalchemy import Column, Integer, String, Boolean, Float, Date, DateTime
from sqlalchemy.sql import func
from database import Base # <-- FIX: Removed the dot from .database

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # --- ADDED: User Profile Fields ---
    user_name = Column(String, default="Sarah") # Default for demo purposes
    has_notifications = Column(Boolean, default=True)
    tuki_score = Column(Integer, default=78)
    
    # --- Onboarding Data Fields ---
    full_name = Column(String)
    date_of_birth = Column(Date)
    sex_assigned_at_birth = Column(String)
    primary_health_goal = Column(String)
    exercise_hours_yesterday = Column(Float)
    sleep_hours_last_night = Column(Float)
    had_sleep_disturbances = Column(Boolean)
    feels_thirsty_at_night = Column(Boolean)
    overall_mood_rating = Column(Integer)
    stress_level = Column(String)
    focus_rating = Column(Integer)
    forgets_things_often = Column(Boolean)
    brain_fog_severity = Column(Integer)
    current_energy_rating = Column(Integer)
    most_energized_time = Column(String)

# --- NEW: Hero Scroller (Goal Cards) ---
class Goal(Base):
    __tablename__ = "goals"
    
    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)

# --- NEW: Today Scroller (Activity Cards) ---
class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    primary_value = Column(String, nullable=False)
    unit_or_status = Column(String)
    description = Column(String, nullable=False)
    background_image_or_gradient = Column(String)

# --- NEW: Digital Twin Suggestions (Content Cards) ---
class Suggestion(Base):
    __tablename__ = "suggestions"
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String, nullable=False)
    star_rating = Column(Float)
    review_count = Column(Integer)
    users_count = Column(Integer)
    description = Column(String, nullable=False)