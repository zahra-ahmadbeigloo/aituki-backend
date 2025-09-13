# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


def normalize_db_url(url: str) -> str:
    # SQLAlchemy needs the 'postgresql+psycopg2' prefix
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg2://", 1)

    # If you accidentally put the external DB URL (public host), require SSL.
    # Internal URLs usually end with `.render.internal` and don't need SSL.
    if "render.internal" not in url and "sslmode" not in url:
        url += ("&" if "?" in url else "?") + "sslmode=require"
    return url

DATABASE_URL = normalize_db_url(os.environ["DATABASE_URL"])

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

