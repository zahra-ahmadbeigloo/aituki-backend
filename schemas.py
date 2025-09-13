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


class UserProfile(BaseModel):
    """Defines the user's profile data for the header."""
    user_name: str
    has_notifications: bool
    tuki_score: int

class Goal(BaseModel):
    """Defines the structure for a single Goal Card in the Hero Scroller."""
    id: int
    image_name: str
    title: str
    subtitle: str
    
    class Config:
        from_attributes = True

class Activity(BaseModel):
    """Defines the structure for a single Activity Card in the Today Scroller."""
    id: int
    title: str
    primary_value: str
    unit_or_status: Optional[str] = None
    description: str
    background_image_or_gradient: Optional[str] = None

    class Config:
        from_attributes = True

class Suggestion(BaseModel):
    """Defines the structure for a single Suggestion Card."""
    id: int
    image_url: Optional[str] = None
    title: str
    star_rating: Optional[float] = None
    review_count: Optional[int] = None
    users_count: Optional[int] = None
    description: str

    class Config:
        from_attributes = True

class HomeScreenResponse(BaseModel):
    """This is the main "contract" for the home screen. 
    It combines all the necessary data into a single, structured response."""
    user_profile: UserProfile
    hero_goals: List[Goal]
    today_activities: List[Activity]
    suggestions: List[Suggestion]
