from sqlalchemy import Column, Integer, String, Text
from src.database.database import Base

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, index=True)
    experience_needed = Column(Integer)
    technical_skill_set = Column(Text)
    vocab_preference = Column(String)
    education_preference = Column(String)
    word_limit = Column(Integer, nullable=True)
    generated_jd = Column(Text, nullable=False, default="Default JD text")  # This will store the generated JD
