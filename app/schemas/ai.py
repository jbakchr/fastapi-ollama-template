from pydantic import BaseModel


class GenerateRequest(BaseModel):
    prompt: str
    model: str | None = None


class GenerateResponse(BaseModel):
    response: str


class PlaygroundRequest(BaseModel):
    prompt: str
    model: str | None = None