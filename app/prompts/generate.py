from app.prompts.base import format_prompt


GENERIC_GENERATE_TEMPLATE = """
You are a helpful AI assistant.

Your task:
{task}

Guidelines:
- Be concise
- Be clear
- Focus on usefulness

Input:
{input}
"""


def build_generate_prompt(task: str, input: str) -> str:
    return format_prompt(
        GENERIC_GENERATE_TEMPLATE,
        task=task,
        input=input,
    )