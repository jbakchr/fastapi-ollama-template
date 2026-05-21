from fastapi import APIRouter
from app.services.ollama_service import OllamaService

router = APIRouter()
ollama = OllamaService()


@router.get("/generate")
def generate(prompt: str):
    response = ollama.generate(prompt)
    return {"response": response}