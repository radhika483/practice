from fastapi import FastAPI
from src.database.database import Base, engine
from src.routers import job_description
import uvicorn 

app = FastAPI(title="JD Generator API", version="1.0")

Base.metadata.create_all(bind=engine)

app.include_router(job_description.router)

@app.get("/")
def root():
    return {"message": "Welcome to the JD Generator API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)



    #hiiii