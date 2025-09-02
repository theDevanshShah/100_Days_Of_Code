"""CLI for ToyPerceptron: train on a sample gate and interactively test inputs."""
from __future__ import annotations

from .perceptron import demo_and_train, Perceptron


def main() -> None:
    print("ToyPerceptron — tiny perceptron demo")
    p = demo_and_train()
    print("Trained. Try inputs like: 0 1 (enter)")
    try:
        while True:
            raw = input("Enter two binary inputs or q to quit: ").strip()
            if raw.lower().startswith("q"):
                break
            parts = raw.split()
            if len(parts) != 2:
                print("Please enter two values.")
                continue
            x = [int(parts[0]), int(parts[1])]
            print("Prediction:", p.predict([x])[0])
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye")


if __name__ == "__main__":
    main()
