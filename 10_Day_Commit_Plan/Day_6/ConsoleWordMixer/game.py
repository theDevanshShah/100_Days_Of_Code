import random
import sys
from typing import List, Tuple


def scramble_word(word: str, seed: int | None = None) -> str:
    """Return a scrambled version of word that is different from original when possible.

    Args:
        word: input word (assumed non-empty).
        seed: optional random seed for reproducible output.

    Returns:
        scrambled word
    """
    if seed is not None:
        rnd = random.Random(seed)
    else:
        rnd = random.Random()

    if len(word) < 2:
        return word

    # Try to produce a different scramble; limit attempts to avoid infinite loop for words with repeated letters
    letters = list(word)
    attempts = 0
    while True:
        attempts += 1
        rnd.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word or attempts >= 10:
            return scrambled


def pick_random_words(source: List[str], count: int, seed: int | None = None) -> List[str]:
    rnd = random.Random(seed)
    if count <= 0:
        return []
    count = min(count, len(source))
    return rnd.sample(source, count)


def play_round(word: str, seed: int | None = None) -> Tuple[bool, str]:
    """Play one console round for a given word.

    Returns (won, scrambled)
    """
    scrambled = scramble_word(word, seed)
    print(f"Scrambled word: {scrambled}")
    guess = input("Your guess: ").strip()
    if guess.lower() == word.lower():
        print("Correct!\n")
        return True, scrambled
    else:
        print(f"Nope — the word was: {word}\n")
        return False, scrambled


def load_default_wordlist() -> List[str]:
    # A short, friendly default list; easy for beginners
    return [
        "python",
        "function",
        "variable",
        "loop",
        "string",
        "integer",
        "module",
        "debug",
        "console",
        "beginner",
    ]


def run_game(rounds: int = 5, seed: int | None = None) -> int:
    """Run the console game for the specified number of rounds.

    Returns the number of correct guesses.
    """
    words = load_default_wordlist()
    chosen = pick_random_words(words, rounds, seed)
    correct = 0
    for i, w in enumerate(chosen, 1):
        print(f"Round {i}/{len(chosen)}")
        won, _ = play_round(w, seed)
        if won:
            correct += 1
    print(f"Game over. You got {correct}/{len(chosen)} correct.")
    return correct


if __name__ == "__main__":
    rounds = 5
    seed = None
    # simple arg parsing
    if len(sys.argv) > 1:
        try:
            rounds = int(sys.argv[1])
        except ValueError:
            pass
    if len(sys.argv) > 2:
        try:
            seed = int(sys.argv[2])
        except ValueError:
            pass
    run_game(rounds, seed)
