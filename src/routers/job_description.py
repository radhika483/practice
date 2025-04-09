from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.schemas.schema import JDRequest, JDResponse
from src.core.job_description import create_jd

router = APIRouter(prefix="/jd", tags=["Job Descriptions"])

@router.post("/", response_model=JDResponse)
def generate_job_description(jd_data: JDRequest, db: Session = Depends(get_db)):
    try:
        jd_entry = create_jd(db, jd_data)
        return jd_entry
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
