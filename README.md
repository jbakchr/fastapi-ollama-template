# fastapi-ollama-template

A minimal FastAPI template for building AI-powered backends using Ollama.

Designed for fast experimentation, reusable prompt patterns, and iterative development.

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

The `/ai/playground` endpoint is your experimentation layer.

- No templates
- No structure
- Just raw input → response

Use it to:

- test prompts quickly
- iterate on ideas
- debug LLM behavior

---

## 🔄 Development Workflow

This project follows a simple prompt evolution flow:

```
playground → logs → feedback → prompts → endpoints
```

1. Experiment in `/ai/playground`
2. Review logs (`logs/ai_logs.jsonl`)
3. Capture insights in `FEEDBACK.md`
4. Refine into reusable prompt templates
5. Expose via API endpoints

See `PROMPT_EVOLUTION.md` for details.

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
- Evolve through real usage, not assumptions

---

## 📚 Project Docs

- `FEEDBACK.md` – prompt experiments and learnings
- `PROMPT_EVOLUTION.md` – how prompts become templates

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
- Designed for local experimentation
- Extend only when needed

---

## 📄 License

MIT
