from fastapi import APIRouter, Depends
import schemas
# NOTE: In the future, you will add `from sqlalchemy.orm import Session` and `from database import get_db`
# to fetch this data from your database. For now, we hardcode it.

router = APIRouter()

@router.get("/home", response_model=schemas.HomeScreenResponse)
def get_home_screen_data():
    # This is placeholder data that matches Bill's design and your schemas
    fake_profile = {"user_name": "Pilar", "has_notifications": True, "tuki_score": 78}
    
    fake_goals = [
        {"id": 1, "title": "Perimenopause tracking", "subtitle": "8 weeks • Day 15", "image_name": "swimmer"},
        {"id": 2, "title": "Yoga and Pilates", "subtitle": "8 weeks • Day 15", "image_name": "yoga"}
    ]
    
    fake_activities = [
        {"id": 1, "title": "Meditation", "primary_value": "20.30", "unit_or_status": "am", "description": "15 min relaxation"}
    ]

    fake_suggestions = [
        {"id": 1, "title": "Hormone therapy", "description": "Practical help and advice...", "star_rating": 4.5, "review_count": 145, "users_count": 1024}
    ]

    return {
        "user_profile": fake_profile,
        "hero_goals": fake_goals,
        "today_activities": fake_activities,
        "suggestions": fake_suggestions
    }
