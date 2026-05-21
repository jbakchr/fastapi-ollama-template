from fastapi import APIRouter

from app.services.ollama_service import OllamaService
from app.schemas.ai import GenerateRequest, GenerateResponse
from app.prompts.generate import build_generate_prompt
from app.prompts.summarize import build_summary_prompt
from app.prompts.classify import build_classification_prompt

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


@router.post("/summarize", response_model=GenerateResponse)
def summarize(request: GenerateRequest):
    prompt = build_summary_prompt(text=request.prompt)

    result = ollama.generate(
        prompt=prompt,
        model=request.model,
    )

    return GenerateResponse(response=result)


@router.post("/classify", response_model=GenerateResponse)
def classify(request: GenerateRequest):
    prompt = build_classification_prompt(
        input=request.prompt,
        categories="""
- question
- statement
- command
- other
""",
    )

    result = ollama.generate(
        prompt=prompt,
        model=request.model,
    )

    return GenerateResponse(response=result)