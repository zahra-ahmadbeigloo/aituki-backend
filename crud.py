from sqlalchemy.orm import Session

# Import your models and schemas from the files you already created.
import models, schemas, security

def get_user_by_email(db: Session, email: str):
    """Fetches a single user from the database by their email."""
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """Creates a new user in the database."""
    # Hash the password before saving it.
    hashed_password = security.get_password_hash(user.password)
    
    # Create a new SQLAlchemy User model instance.
    # We exclude the plain password and add the hashed one.
    db_user = models.User(
        email=user.email, 
        hashed_password=hashed_password,
        **user.dict(exclude={"email", "password"}) # Add all other onboarding fields
    )
    
    # Add the new user to the session and commit it to the database.
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Refresh the instance to get the new ID.
    
    return db_user
