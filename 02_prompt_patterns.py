from rich.console import Console
from rich.panel import Panel

from workshop_client import ask_llm

console = Console()

sample_text = """
Large language models can summarize, classify, extract, and generate text.
But their output quality depends heavily on the prompt, the provided context,
and the clarity of the expected format.
""".strip()

prompts = [
    (
        "Generic prompt",
        f"Summarize this:\n\n{sample_text}",
    ),
    (
        "Audience-aware prompt",
        f"Summarize this in 3 bullet points for a beginner who knows Python but is new to AI:\n\n{sample_text}",
    ),
    (
        "Action-oriented prompt",
        f"From the text below, extract 3 practical lessons a student can apply while building with LLMs.\nReturn short bullet points.\n\n{sample_text}",
    ),
]

for title, user_prompt in prompts:
    answer = ask_llm(
        [
            {"role": "system", "content": "You are a helpful workshop instructor."},
            {"role": "user", "content": user_prompt},
        ]
    )
    console.print(Panel(answer, title=title, expand=False))
