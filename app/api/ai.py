from fastapi import APIRouter

from app.services.ollama_service import OllamaService
from app.schemas.ai import GenerateRequest, GenerateResponse

router = APIRouter()
ollama = OllamaService()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    result = ollama.generate(
        prompt=request.prompt,
        model=request.model if request.model else None,
    )
    return GenerateResponse(response=result)