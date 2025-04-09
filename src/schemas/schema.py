from pydantic import BaseModel, Field
from typing import Optional

class JDRequest(BaseModel):
    job_title: str = Field(..., example="Software Engineer")
    experience_needed: int = Field(..., example=3)
    technical_skill_set: str = Field(..., example="Python, FastAPI, PostgreSQL")
    vocab_preference: str = Field(..., example="Medium")
    education_preference: str = Field(..., example="Bachelor’s in Computer Science")
    word_limit: Optional[int] = Field(None, example=200)
class JDResponse(BaseModel):
    id: int
    job_title: str
    experience_needed: int
    technical_skill_set: str
    vocab_preference: str
    education_preference: str
    word_limit: Optional[int]
    generated_jd: str
