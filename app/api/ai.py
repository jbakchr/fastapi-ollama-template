from fastapi import APIRouter

from app.services.ollama_service import OllamaService
from app.schemas.ai import GenerateRequest, GenerateResponse
from app.prompts.generate import build_generate_prompt

router = APIRouter()
ollama = OllamaService()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    prompt = build_generate_prompt(
        task="Generate a useful response",
        input=request.prompt,
    )

    result = ollama.generate(
        prompt=prompt,
        model=request.model,
    )

    return GenerateResponse(response=result)