from app.prompts.base import format_prompt


SUMMARY_TEMPLATE = """
You are a helpful assistant.

Summarize the following text.

Instructions:
- Be concise
- Use bullet points if helpful
- Focus on key information

Text:
{text}
"""


def build_summary_prompt(text: str) -> str:
    return format_prompt(
        SUMMARY_TEMPLATE,
        text=text,
    )