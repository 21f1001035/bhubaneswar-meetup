import argparse
from rich.console import Console
from rich.table import Table

from workshop_client import ask_llm, DEFAULT_MODEL

console = Console()

parser = argparse.ArgumentParser(description="Compare outputs across multiple models.")
parser.add_argument(
    "--models",
    nargs="+",
    default=[DEFAULT_MODEL],
    help="List of models to compare",
)
parser.add_argument(
    "--prompt",
    default="Explain retrieval-augmented generation in 4 lines for a student workshop.",
)
args = parser.parse_args()

table = Table(title="Model Comparison")
table.add_column("Model", style="cyan", width=22)
table.add_column("Response", style="white", width=90)

for model in args.models:
    output = ask_llm(
        [
            {"role": "system", "content": "You are a concise AI tutor."},
            {"role": "user", "content": args.prompt},
        ],
        model=model,
        temperature=0.2,
    )
    table.add_row(model, output)

console.print(table)
