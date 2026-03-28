import json
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from rag_utils import load_and_chunk, retrieve_top_k
from workshop_client import ask_llm

console = Console()

handbook_path = Path("data/program_handbook.md")
questions_path = Path("data/rag_questions.json")

chunks = load_and_chunk(handbook_path)

sample_questions = json.loads(questions_path.read_text(encoding="utf-8"))
question = sample_questions[0]["question"]

top_chunks = retrieve_top_k(question, chunks, k=3)
context = "\n\n---\n\n".join(
    [f"[Chunk {item['chunk_id']} | score={item['score']:.3f}]\n{item['text']}" for item in top_chunks]
)

messages = [
    {
        "role": "system",
        "content": (
            "Answer only from the provided context. "
            "If the answer is not in the context, say 'I do not know from the handbook.'"
        ),
    },
    {
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {question}",
    },
]

answer = ask_llm(messages, temperature=0)

console.print(Panel(question, title="Question", expand=False))
console.print(Panel(context, title="Retrieved context", expand=False))
console.print(Panel(answer, title="Grounded answer", expand=False))
