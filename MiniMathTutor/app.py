"""MiniMathTutor: a beginner-friendly console math quiz app.

Features:
- Generates simple arithmetic exercises (addition, subtraction, multiplication, division).
- Tracks score and time per question.
- Difficulty scales by number of digits.
"""
from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Tuple, Callable


@dataclass
class Question:
    text: str
    answer: float
    formatter: Callable[[float], str] = lambda x: str(int(x)) if float(x).is_integer() else f"{x:.2f}"


def generate_question(difficulty: int = 1) -> Question:
    """Generate a random arithmetic question.

    difficulty: 1 (easy) -> numbers 0-10
                2 (medium) -> numbers 0-50
                3 (hard) -> numbers 0-200
    Returns a Question object.
    """
    if difficulty <= 1:
        max_n = 10
    elif difficulty == 2:
        max_n = 50
    else:
        max_n = 200

    op = random.choice(["+", "-", "*", "/"])
    a = random.randint(0, max_n)
    b = random.randint(1 if op == "/" else 0, max_n)

    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    else:
        # produce a division that isn't too ugly: use round to 2 decimals
        ans = round(a / b, 2)

    text = f"{a} {op} {b} = ?"
    return Question(text=text, answer=ans)


def ask_question(q: Question, time_limit: float | None = None) -> Tuple[bool, float]:
    """Ask a question on the console, return (is_correct, seconds_taken).

    time_limit: optional limit in seconds for the answer; None means no limit.
    """
    print(q.text)
    start = time.time()
    try:
        user = input("Your answer: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting the quiz.")
        raise
    elapsed = time.time() - start

    if time_limit is not None and elapsed > time_limit:
        print(f"Time's up! You took {elapsed:.1f}s (limit {time_limit}s).")
        return False, elapsed

    # try to parse number
    try:
        user_val = float(user)
    except ValueError:
        print("Invalid number format.")
        return False, elapsed

    # compare with tolerance for floats
    is_correct = abs(user_val - q.answer) < 1e-2
    return is_correct, elapsed


def run_quiz(rounds: int = 5, difficulty: int = 1, time_limit: float | None = None) -> dict:
    """Run a quiz session and return stats.

    Returns a dict: {"asked": int, "correct": int, "total_time": float}
    """
    stats = {"asked": 0, "correct": 0, "total_time": 0.0}
    print("Welcome to MiniMathTutor — practice basic arithmetic in the console.")
    print(f"Rounds: {rounds}, Difficulty: {difficulty}, Time limit: {time_limit or 'None'}s")

    for i in range(rounds):
        q = generate_question(difficulty)
        stats["asked"] += 1
        try:
            correct, t = ask_question(q, time_limit=time_limit)
        except (KeyboardInterrupt, EOFError):
            break
        stats["total_time"] += t
        if correct:
            stats["correct"] += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. Answer: {q.answer}\n")

    print("Quiz finished.")
    print(f"Score: {stats['correct']}/{stats['asked']} in {stats['total_time']:.1f}s")
    return stats


def main() -> None:
    print("MiniMathTutor CLI")
    try:
        rounds_s = input("How many questions would you like? [5]: ") or "5"
        rounds = int(rounds_s)
    except ValueError:
        rounds = 5

    try:
        diff_s = input("Difficulty 1-easy,2-medium,3-hard [1]: ") or "1"
        difficulty = int(diff_s)
        if difficulty not in (1, 2, 3):
            difficulty = 1
    except ValueError:
        difficulty = 1

    try:
        tlim_s = input("Time limit per question in seconds (empty = no limit): ")
        time_limit = float(tlim_s) if tlim_s.strip() != "" else None
    except ValueError:
        time_limit = None

    run_quiz(rounds=rounds, difficulty=difficulty, time_limit=time_limit)


if __name__ == "__main__":
    main()
