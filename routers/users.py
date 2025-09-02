from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Import all the necessary components from your other files.
import crud, models, schemas
from database import SessionLocal, engine

# Create the database tables if they don't exist.
# models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency: This function will create a new database session for each request
# and close it when it's done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/register", response_model=schemas.User) # You'll need a User response schema
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    API endpoint to register a new user.
    """
    # First, check if a user with this email already exists.
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # If not, create the new user.
    return crud.create_user(db=db, user=user)