#!/usr/bin/env python3
"""
Simple console math quiz for kids.
- Run interactively with: python3 game.py
- Contains a quick_self_test() used for non-interactive verification.
"""
import random
import operator

OPERATIONS = {
    '1': ('Addition', '+', operator.add),
    '2': ('Subtraction', '-', operator.sub),
    '3': ('Multiplication', '×', operator.mul),
    '4': ('Division', '÷', operator.floordiv),
}


def generate_question(level=1):
    """Return a dict with question text and the integer answer."""
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == 2:
        a, b = random.randint(5, 20), random.randint(1, 12)
    else:
        a, b = random.randint(10, 50), random.randint(2, 20)

    op_key = random.choice(list(OPERATIONS.keys()))
    name, symbol, fn = OPERATIONS[op_key]

    # For division, make numbers divisible to keep answers simple
    if fn == operator.floordiv:
        b = random.randint(1, 10)
        a = b * random.randint(1, 10)

    question = f"What is {a} {symbol} {b}?"
    answer = fn(a, b)
    return {"name": name, "question": question, "answer": answer, "a": a, "b": b, "symbol": symbol}


def ask_question_interactive(q):
    print(q["question"])
    resp = input("Answer: ").strip()
    try:
        if int(resp) == q["answer"]:
            print("Correct! 🎉")
            return True
        else:
            print(f"Not quite — the answer is {q['answer']}.")
            return False
    except Exception:
        print(f"That's not a number. The answer was {q['answer']}.")
        return False


def start_game():
    print("Math Fun — quick quiz")
    print("Answer 5 questions. Try your best!")
    score = 0
    for i in range(5):
        q = generate_question()
        if ask_question_interactive(q):
            score += 1
    print(f"Your score: {score}/5. Well done!")


def quick_self_test():
    """Non-interactive quick check used for CI or automation.
    Returns True when basic behaviour is correct.
    """
    random.seed(0)
    q = generate_question()
    # Basic checks: question is a string and answer is an int
    return isinstance(q.get("question"), str) and isinstance(q.get("answer"), int)


if __name__ == '__main__':
    start_game()
