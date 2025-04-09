import ollama
from src.models.model import JobDescription
from sqlalchemy.orm import Session
from src.schemas.schema import JDRequest

def generate_jd(prompt: str) -> str:
    response = ollama.chat(model="llama2:7b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def create_jd(db: Session, jd_data: JDRequest):
    prompt = f"""
    Generate a job description for the following:
    - Job Title: {jd_data.job_title}
    - Experience Needed: {jd_data.experience_needed} years
    - Technical Skills: {jd_data.technical_skill_set}
    - Vocab Preference: {jd_data.vocab_preference}
    - Education: {jd_data.education_preference}
    - Word Limit: {jd_data.word_limit if jd_data.word_limit else 'No limit'}
    Ensure the JD is engaging, informative, and follows industry standards.
    """

    generated_text = generate_jd(prompt)
    print("Hellog",generated_text)  # Debugging log
    
    jd_entry = JobDescription(
        job_title=jd_data.job_title,
        experience_needed=jd_data.experience_needed,
        technical_skill_set=jd_data.technical_skill_set,
        vocab_preference=jd_data.vocab_preference,
        education_preference=jd_data.education_preference,
        word_limit=jd_data.word_limit,
        generated_jd=generated_text
    )

    db.add(jd_entry)
    db.commit()
    db.refresh(jd_entry)
    print(f"JD Created with ID: {jd_entry.generated_jd}")  # Debugging log
    return jd_entry
