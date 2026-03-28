from rich.console import Console
from rich.pretty import Pretty

from workshop_client import ask_json

console = Console()

ticket = """
Hi team, I missed the quiz because my home internet was down for two days.
The quiz window closed yesterday night. Can I get another attempt?
My course is Intro to Data Science.
""".strip()

messages = [
    {
        "role": "system",
        "content": (
            "You are an operations assistant. "
            "Return valid JSON only. "
            "Use this schema: "
            '{"category": str, "priority": "low|medium|high", "needs_human_review": bool, '
            '"student_problem": str, "draft_reply": str}'
        ),
    },
    {
        "role": "user",
        "content": f"Read the ticket and extract the fields.\n\nTicket:\n{ticket}",
    },
]

result = ask_json(messages)

console.print("[bold green]Structured result[/bold green]")
console.print(Pretty(result))
