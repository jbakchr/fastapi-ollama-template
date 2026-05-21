# PROMPT_EVOLUTION.md

Guidelines for how prompts evolve from experimentation into reusable templates.

---

## 🧭 Overview

Not every prompt should become a template.

This project follows a simple lifecycle:

```

experiment → identify → refine → promote → reuse

```

---

## 🧪 1. Experiment (Playground)

Use `/ai/playground` to:

- try ideas
- tweak wording
- explore different structures

At this stage:

- no structure required
- fast iteration is the goal

---

## 🔍 2. Identify (Logs + FEEDBACK.md)

After experimenting, review:

- logs (`logs/ai_logs.jsonl`)
- entries in `FEEDBACK.md`

A prompt is worth keeping if:

- it produces consistently good output
- it solves a real use-case
- it has been used more than once
- it required refinement to work well

---

## 🛠️ 3. Refine (Make reusable)

Take a working prompt and:

- remove hardcoded details
- generalize wording
- add light structure

Example:

Before:

```

Summarize this in 3 bullet points:

```

After:

```

Summarize the following text.

Instructions:

- Use 2–4 bullet points
- Be concise
- Focus on key information

Text:
{text}

```

---

## 🚀 4. Promote (Template + Endpoint)

When a prompt becomes stable:

1. Move it into `app/prompts/`
2. Add a builder function
3. Optionally expose it via an API endpoint

---

## ✅ Promotion Rule

Promote a prompt to a template if:

- it has been used 2–3 times
- it has been refined at least once
- it solves a clear task

---

## ❌ Keep in Playground if

- it is a one-off experiment
- results are inconsistent
- the use-case is unclear

---

## 🧠 Heuristic

Ask:

> “Would future me be annoyed rewriting this?”

If yes → promote it

---

## 🏷️ Optional tagging (FEEDBACK.md)

When experimenting, use simple tags:

- `[KEEP]` → good candidate for template
- `[REFINE]` → needs improvement
- `[DROP]` → not useful

---

## 🧩 Common Template Candidates

Typical reusable prompt categories:

- summarize
- classify
- extract
- transform / rewrite
- microsteps

---

## 🧠 Philosophy

- Start messy (playground)
- Learn from real usage
- Only promote what proves useful
- Avoid premature abstraction

---
