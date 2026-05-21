from app.prompts.base import format_prompt


EXTRACT_TEMPLATE = """
Extract the following information from the text.

Fields:
{fields}

Text:
{text}

Return the result in a structured JSON format.
"""


def build_extract_prompt(text: str, fields: str) -> str:
    return format_prompt(
        EXTRACT_TEMPLATE,
        text=text,
        fields=fields,
    )