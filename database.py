# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///registration.db"  # SQLite database file

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session factory
Session = sessionmaker(bind=engine)

def create_tables():
    """Creates the database tables."""
    Base.metadata.create_all(engine)

def get_session():
    """Returns a new session object."""
    return Session()
