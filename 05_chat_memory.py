from rich.console import Console
from rich.panel import Panel

from workshop_client import ask_llm

console = Console()

history = [
    {
        "role": "system",
        "content": "You are a friendly workshop chatbot that helps students learn LLMs with Python.",
    }
]

console.print("[bold cyan]Type 'exit' to stop.[/bold cyan]")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break

    history.append({"role": "user", "content": user_input})
    answer = ask_llm(history, max_tokens=500)
    history.append({"role": "assistant", "content": answer})
    console.print(Panel(answer, title="Assistant", expand=False))
