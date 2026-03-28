import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from rag_utils import load_and_chunk, retrieve_top_k
from workshop_client import ask_json

console = Console()

tickets_path = Path("data/student_support_tickets.jsonl")
handbook_path = Path("data/program_handbook.md")
output_path = Path("outputs/case_study_predictions.jsonl")

chunks = load_and_chunk(handbook_path, chunk_size=800, overlap=120)

tickets = []
for line in tickets_path.read_text(encoding="utf-8").splitlines():
    if line.strip():
        tickets.append(json.loads(line))

results = []

for ticket in tickets:
    retrieved = retrieve_top_k(ticket["message"], chunks, k=2)
    context = "\n\n---\n\n".join(
        [f"[Chunk {item['chunk_id']}]\n{item['text']}" for item in retrieved]
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an academic support copilot. "
                "Use only the handbook context. "
                "Return valid JSON only with this schema: "
                '{"ticket_id": str, "category": str, "priority": "low|medium|high", '
                '"needs_human_review": bool, "policy_basis": str, "draft_reply": str}'
            ),
        },
        {
            "role": "user",
            "content": (
                f"Handbook context:\n{context}\n\n"
                f"Ticket ID: {ticket['ticket_id']}\n"
                f"Student message: {ticket['message']}\n\n"
                "Classify the ticket, assign a priority, state the policy basis briefly, "
                "and draft a helpful reply."
            ),
        },
    ]

    result = ask_json(messages, temperature=0)
    results.append(result)

with output_path.open("w", encoding="utf-8") as f:
    for item in results:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

table = Table(title="Student Support Copilot - Predictions")
table.add_column("Ticket")
table.add_column("Category")
table.add_column("Priority")
table.add_column("Human review?")
table.add_column("Policy basis")

for item in results:
    table.add_row(
        item["ticket_id"],
        item["category"],
        item["priority"],
        str(item["needs_human_review"]),
        item["policy_basis"][:90],
    )

console.print(table)
console.print(f"\nSaved outputs to: {output_path}")
