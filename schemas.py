from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    date_of_birth: date
    sex_assigned_at_birth: str
    primary_health_goal: Optional[str] = None
    exercise_hours_yesterday: float
    sleep_hours_last_night: float
    had_sleep_disturbances: bool
    feels_thirsty_at_night: bool
    overall_mood_rating: int
    stress_level: str
    focus_rating: int
    forgets_things_often: bool
    brain_fog_severity: int
    current_energy_rating: int
    most_energized_time: str

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    full_name: str
    
    class Config:
        from_attributes = True

# --- NEW: Schemas for Authentication ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None