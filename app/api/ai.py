from fastapi import APIRouter

from app.services.ollama_service import OllamaService
from app.schemas.ai import GenerateRequest, GenerateResponse, PlaygroundRequest
from app.prompts.generate import build_generate_prompt
from app.prompts.summarize import build_summary_prompt
from app.prompts.classify import build_classification_prompt
from app.prompts.extract import build_extract_prompt

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


@router.post("/extract", response_model=GenerateResponse)
def extract(request: GenerateRequest):
    prompt = build_extract_prompt(
        text=request.prompt,
        fields="""
- name
- date
- location
- key_points
""",
    )

    result = ollama.generate(
        prompt=prompt,
        model=request.model,
    )

    return GenerateResponse(response=result)


@router.post("/playground", response_model=GenerateResponse)
def playground(request: PlaygroundRequest):
    result = ollama.generate(
        prompt=request.prompt,
        model=request.model,
    )

    return GenerateResponse(response=result)