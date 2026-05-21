import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/ai_logs.jsonl")


def log_interaction(endpoint: str, prompt: str, response: str):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "endpoint": endpoint,
        "prompt": prompt,
        "response": response,
    }

    # Ensure logs folder exists
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")