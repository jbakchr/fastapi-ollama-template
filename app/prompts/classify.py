from app.prompts.base import format_prompt


CLASSIFY_TEMPLATE = """
You are a classification assistant.

Classify the following input into one of these categories:
{categories}

Input:
{input}

Return only the category name.
"""


def build_classification_prompt(input: str, categories: str) -> str:
    return format_prompt(
        CLASSIFY_TEMPLATE,
        input=input,
        categories=categories,
    )
