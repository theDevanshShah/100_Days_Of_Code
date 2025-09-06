"""DailySparks core functionality

Provides quick daily "sparks" (micro-challenges), simple persistence for favorites,
and a tiny CLI-friendly API.
"""
from __future__ import annotations

import json
import random
from pathlib import Path
from typing import List

DATA_DIR = Path(__file__).parent / "data"
FAV_FILE = DATA_DIR / "favorites.json"

SPARKS = [
    "Drink a full glass of water right now.",
    "Take a 5-minute walk outside and notice 3 new things.",
    "Declutter one small area (desktop, drawer) for 10 minutes.",
    "Send a quick message to someone you appreciate.",
    "Try a 2-minute breathing exercise (inhale 4s, hold 4s, exhale 6s).",
    "Write one sentence about something you're grateful for.",
    "Stand and stretch for 2 minutes: neck, shoulders, back.",
    "Make a tiny to-do list of 3 achievable items for the next hour.",
    "Prepare a healthy snack and savour it mindfully.",
    "Spend 3 minutes learning one new word and use it in a sentence.",
]


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_spark(seed: int | None = None) -> str:
    """Return a random micro-challenge (spark).

    If seed is provided, selection is deterministic.
    """
    rng = random.Random(seed)
    return rng.choice(SPARKS)


def _read_favorites() -> List[str]:
    _ensure_data_dir()
    if not FAV_FILE.exists():
        return []
    try:
        with FAV_FILE.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return [str(x) for x in data]
    except Exception:
        return []
    return []


def _write_favorites(items: List[str]) -> None:
    _ensure_data_dir()
    with FAV_FILE.open("w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=2)


def add_favorite(spark: str) -> None:
    """Add a spark to favorites if not already present."""
    items = _read_favorites()
    if spark in items:
        return
    items.append(spark)
    _write_favorites(items)


def list_favorites() -> List[str]:
    """Return favorite sparks in insertion order."""
    return _read_favorites()


if __name__ == "__main__":
    print(get_spark())
