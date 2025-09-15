"""Tests for Day 4 loop utilities."""
import importlib.util
from pathlib import Path

# Load the module by file path because the parent folder name starts with a
# digit which is not a valid Python package name. Loading by path keeps the
# tests runnable in-place.
mod_path = Path(__file__).resolve().parent / "loops.py"
spec = importlib.util.spec_from_file_location("day4.loops", str(mod_path))
loops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loops)


def test_sum_range_happy_path():
    assert loops.sum_range(1, 5) == 15
    assert loops.sum_range(-2, 2) == -2


def test_sum_range_empty():
    assert loops.sum_range(5, 1) == 0


def test_first_multiples():
    assert loops.first_multiples(3, 4) == [3, 6, 9, 12]
    assert loops.first_multiples(5, 0) == []


def test_repeat_until_runs_and_stops():
    state = {"count": 0}

    def pred():
        return state["count"] >= 3

    def act():
        state["count"] += 1

    iters = loops.repeat_until(pred, act, max_iters=10)
    assert iters == 3
    assert state["count"] == 3


def test_repeat_until_max_iters():
    state = {"count": 0}

    def pred():
        return False

    def act():
        state["count"] += 1

    iters = loops.repeat_until(pred, act, max_iters=5)
    assert iters == 5
    assert state["count"] == 5
