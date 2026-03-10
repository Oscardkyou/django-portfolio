from __future__ import annotations

import json
import logging
from typing import Final
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

LOGGER = logging.getLogger(__name__)
OLLAMA_URL: Final[str] = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL: Final[str] = "tinyllama"
AI_UNAVAILABLE_MESSAGE: Final[str] = "AI assistant is temporarily unavailable"


def _build_prompt(message: str, language: str) -> str:
    response_language = "Russian" if language == "ru" else "English"
    fallback_message = (
        "Я могу отвечать только на основе данных из портфолио Даурена Аскарова."
        if language == "ru"
        else "I can only answer based on Dauren Askarov's portfolio data."
    )

    return f"""You are an assistant describing the experience of Dauren Askarov.

Dauren Askarov is a Python Backend Engineer specializing in AI systems.

Portfolio facts:
- Gravora: RAG internal ChatGPT system, Telegram bot integration, FastAPI backend, ChromaDB, Redis, OpenAI, Hugging Face
- 5Dhub: API gateway, blockchain monitoring, computer vision, CI/CD improvements
- Neobis: Django backend development, code review, mentoring, tender platform backend
- Core technologies: Python, FastAPI, Django, PostgreSQL, Redis, Docker, AWS, AI systems, WebSockets, Prometheus, Grafana

Rules:
- Answer only using the portfolio facts above.
- Do not invent companies, metrics, projects, tools, or responsibilities.
- If the question is not covered by the portfolio facts, reply exactly: {fallback_message}
- Keep the answer short, professional, and concrete.
- Respond only in {response_language}.

User question: {message.strip()}
"""


def ask_ai(message: str, language: str = "en") -> str:
    prompt = _build_prompt(message=message, language=language)
    payload = json.dumps(
        {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        }
    ).encode("utf-8")
    request = Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=60) as response:
            response_body = response.read().decode("utf-8")
        response_payload = json.loads(response_body)
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        LOGGER.warning("Ollama request failed", exc_info=exc)
        return AI_UNAVAILABLE_MESSAGE

    answer = str(response_payload.get("response", "")).strip()
    return answer or AI_UNAVAILABLE_MESSAGE
