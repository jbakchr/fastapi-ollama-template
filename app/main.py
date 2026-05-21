from dotenv import load_dotenv
from fastapi import FastAPI

from app.api import ai

load_dotenv()

app = FastAPI()

app.include_router(ai.router, prefix="/ai")

@app.get("/")
def root():
    return {"message": "FastAPI + Ollama template is running 🚀"}
