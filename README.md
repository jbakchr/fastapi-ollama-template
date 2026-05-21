# fastapi-ollama-template

A minimal FastAPI template with Ollama integration.
Use this as a starting point for AI-powered backend projects.

## Quick start

```sh
git clone <your repo>

pip install -r requirements.txt

cp .env.example .env

uvicorn app.main:app --reload
```

## Example

```
GET /ai/generate?prompt=hello
```

## Philosophy

- Minimal and fast to start
- Designed for iterative AI experiments
- Easy to extend