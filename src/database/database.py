from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure DATABASE_URL is not None
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file or environment variables.")

# Debugging: Print DATABASE_URL to verify it's loaded correctly
print(f"Database URL: {DATABASE_URL}")

# SQLAlchemy Engine and Session
engine = create_engine(DATABASE_URL)  # Ensured to be a valid string
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from dotenv import load_dotenv
# import os

# # Load environment variables from the specific .env file
# load_dotenv(r"E:\JD-Project\.env")  # Use raw string

# # Debug: Print all environment variables
# print("Environment Variables:")
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# # Fetch DATABASE_URL from .env
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Debug: Print the DATABASE_URL to confirm it's loaded correctly
# print(f"Database URL: {DATABASE_URL}")