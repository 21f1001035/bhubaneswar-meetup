from rich.console import Console
from rich.panel import Panel

from workshop_client import ask_llm, DEFAULT_MODEL

console = Console()

messages = [
    {
        "role": "system",
        "content": "You are a concise teaching assistant for beginners learning AI.",
    },
    {
        "role": "user",
        "content": "Explain what an LLM is in exactly 3 bullet points for a first-year college student.",
    },
]

answer = ask_llm(messages, model=DEFAULT_MODEL)

console.print(Panel.fit(answer, title=f"Model response ({DEFAULT_MODEL})"))
