# ROADMAP.md

Possible future evolution of the fastapi-ollama-template.

This is not a strict plan — only ideas based on real usage and needs.

---

## ✅ Current State

- FastAPI backend skeleton
- Ollama integration
- Prompt template system
- Core endpoints (generate, summarize, classify, extract)
- Playground endpoint
- Logging (JSONL)
- Feedback + prompt evolution workflow

---

## 🔜 Next Possible Improvements

### Prompt System

- Improve prompt templates
- Add more categories (transform, rewrite, microsteps)
- Introduce versioning for prompts (optional)

---

### API Improvements

- Structured responses (especially for `/extract`)
- Better request schemas per endpoint
- Error handling and validation

---

### Developer Experience

- Setup script (`start.sh`)
- CLI support (optional)
- Docker setup

---

### LLM Features

- Streaming responses
- Support for multiple models
- Configurable inference options

---

### Logging & Feedback

- Improve log structure
- Add log filtering / tooling
- Better integration with FEEDBACK.md

---

## 🧠 Guiding Principle

Only implement improvements when they are:

- used more than once
- clearly valuable
- simple to maintain

Avoid adding complexity upfront.

---

## 🚀 Long-Term Ideas

- Turn template into a reusable package
- Provide example projects using the template
- Share prompt patterns publicly

---
