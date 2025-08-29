Kids Console Math Game

A tiny, console-based math quiz for kids. It's designed to be simple and friendly.

How to run

- Open a terminal in the project folder and run:

    python3 game.py

What it does

- Asks 5 simple arithmetic questions (addition, subtraction, multiplication, division).
- Gives immediate feedback for each answer and a final score.

Quick self-test (non-interactive)

You can run a quick automated check (useful in CI) which will import the game and call a small test helper:

    python3 -c "import sys; sys.path.insert(0, '/Users/devanshshah/Developer/Youtube/100DaysOfCode/100_Days_Of_Code'); from KidsConsoleApp import game; print(game.quick_self_test())"

This should print True if the basic behaviour is OK.

Notes

- The interactive game is kid-friendly and keeps numbers small for easier mental math.
- Feel free to expand levels, add high-score persistence, or a timed mode as follow-ups.
