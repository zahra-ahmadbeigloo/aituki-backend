from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- FIX: Added the port number :5432 after the address ---
# Make sure to replace YOUR_PASSWORD with your actual password.
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:4900946559Dz@127.0.0.1:5432/aituki_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
