# fastapi-ollama-template

A minimal FastAPI template for building AI-powered backends using Ollama.

Designed for fast experimentation, reusable prompt patterns, and simple iteration.

---

## 🚀 Features

- ✅ FastAPI backend skeleton
- ✅ Ollama integration (local LLMs)
- ✅ Prompt template system
- ✅ Prebuilt AI endpoints:
  - `/ai/generate` – generic generation
  - `/ai/summarize` – summarize text
  - `/ai/classify` – classify input
  - `/ai/extract` – extract structured data
  - `/ai/playground` – experiment with prompts
- ✅ JSONL logging of prompt/response interactions

---

## ⚡ Quickstart

```bash
git clone <your-repo-url>

cd fastapi-ollama-template

pip install -r requirements.txt

cp .env.example .env

uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

## 🧠 Example Usage

### Summarize

POST `/ai/summarize`

```json
{
  "prompt": "FastAPI is a modern, fast web framework for building APIs with Python."
}
```

---

### Playground

POST `/ai/playground`

```json
{
  "prompt": "Explain FastAPI like I'm 12"
}
```

---

## 🧩 Project Structure

```
app/
  api/            # API endpoints
  prompts/        # Prompt templates
  schemas/        # Pydantic models
  services/       # Ollama integration
  utils/          # Logging utilities

logs/             # Local prompt/response logs (ignored by git)
```

---

## 🧪 Prompt System

Prompts are stored as reusable building blocks:

```
app/prompts/
  summarize.py
  classify.py
  extract.py
```

Each prompt:

- defines a template
- provides a builder function

This makes prompts reusable, testable, and easy to evolve.

---

## 🧪 Playground Endpoint

The `/ai/playground` endpoint allows direct prompt experimentation:

- No templates
- No structure
- Just raw input → response

Use it to:

- test prompts quickly
- iterate on ideas
- debug LLM behavior

---

## 📝 Logging

All interactions are logged locally in:

```
logs/ai_logs.jsonl
```

Each entry contains:

- timestamp
- endpoint
- prompt
- response

This helps:

- improve prompts over time
- debug outputs
- build datasets

---

## 💡 Philosophy

- Minimal and fast to start
- Built for experimentation and iteration
- Prompt-first design
- Avoid overengineering
- Designed to evolve through real usage

---

## 📦 Usage as Template

This repository is a GitHub template.

👉 Click **"Use this template"** to create a new project with the same structure.

---

## 🔧 Requirements

- Python 3.10+
- Ollama running locally

---

## 📌 Notes

- Logs are ignored via `.gitignore`
- Designed for local development and experimentation
- Extend based on real needs (not upfront complexity)

---

## 📄 License

MIT
