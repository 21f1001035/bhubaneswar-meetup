from __future__ import annotations

from pathlib import Path
from typing import List, Dict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 120) -> List[str]:
    text = text.strip()
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += chunk_size - overlap
    return [c for c in chunks if c]


def load_and_chunk(path: str | Path, chunk_size: int = 700, overlap: int = 120) -> List[Dict]:
    text = Path(path).read_text(encoding="utf-8")
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    return [{"chunk_id": i + 1, "text": chunk} for i, chunk in enumerate(chunks)]


def retrieve_top_k(question: str, chunks: List[Dict], k: int = 3) -> List[Dict]:
    corpus = [c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(corpus + [question])
    question_vec = matrix[-1]
    chunk_vecs = matrix[:-1]
    scores = cosine_similarity(question_vec, chunk_vecs).flatten()
    ranked = sorted(
        [
            {
                "chunk_id": chunks[i]["chunk_id"],
                "text": chunks[i]["text"],
                "score": float(scores[i]),
            }
            for i in range(len(chunks))
        ],
        key=lambda x: x["score"],
        reverse=True,
    )
    return ranked[:k]
