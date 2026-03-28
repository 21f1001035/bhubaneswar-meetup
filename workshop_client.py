import json
import os
from typing import List, Dict, Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEFAULT_MODEL = os.getenv("MODEL", "gpt-4o-mini")
DEFAULT_TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))


def get_client() -> OpenAI:
    base_url = os.getenv("OPENAI_BASE_URL")
    kwargs = {}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"), **kwargs)


def ask_llm(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: int = 700,
) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model=model or DEFAULT_MODEL,
        temperature=DEFAULT_TEMPERATURE if temperature is None else temperature,
        max_tokens=max_tokens,
        messages=messages,
    )
    return response.choices[0].message.content or ""


def ask_json(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = 0,
    max_tokens: int = 700,
):
    raw = ask_llm(messages=messages, model=model, temperature=temperature, max_tokens=max_tokens)
    cleaned = raw.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.removeprefix("```json").removesuffix("```").strip()
    elif cleaned.startswith("```"):
        cleaned = cleaned.removeprefix("```").removesuffix("```").strip()

    return json.loads(cleaned)
