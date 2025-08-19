#!/usr/bin/env python3
"""
youtube_tutorial.py

Small, self-contained Python examples you can teach on YouTube.

Contains short snippets that demonstrate:
- list basics and list comprehensions
- map/filter and lambda usage
- generator (fibonacci) and memory benefits
- simple prime sieve
- a tiny class example
- basic error handling
- a minimal CLI to run the demos

Run directly: python3 youtube_tutorial.py --demo all
"""
from __future__ import annotations

import argparse
import math
from typing import Iterable, List


def list_examples() -> None:
    """Show list operations and comprehensions."""
    nums = [1, 2, 3, 4, 5]
    print("Original list:", nums)

    # List comprehension: square each number
    squares = [n * n for n in nums]
    print("Squares (list comprehension):", squares)

    # Filter + map style using comprehensions
    evens = [n for n in nums if n % 2 == 0]
    print("Evens (filter):", evens)

    # Using map/filter with lambda (equivalent)
    doubled = list(map(lambda x: x * 2, nums))
    print("Doubled (map + lambda):", doubled)


def fibonacci_generator(n: int) -> Iterable[int]:
    """Yield first n Fibonacci numbers lazily.

    Demonstrates generators for large sequences without using lots of memory.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def show_fibonacci(n: int = 10) -> None:
    print(f"First {n} Fibonacci numbers (generator):")
    for idx, v in enumerate(fibonacci_generator(n), 1):
        print(f"{idx}: {v}")


def sieve_primes(limit: int) -> List[int]:
    """Return primes up to limit using Sieve of Eratosthenes (inclusive).

    Simple, fast enough for small demos.
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.sqrt(limit)) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


class SimpleCounter:
    """Tiny example of a class with a counter and a couple of methods."""

    def __init__(self, start: int = 0) -> None:
        self.count = int(start)

    def inc(self, by: int = 1) -> None:
        if by < 0:
            raise ValueError("increment must be non-negative")
        self.count += by

    def reset(self) -> None:
        self.count = 0

    def __repr__(self) -> str:  # nice printable representation for demos
        return f"SimpleCounter(count={self.count})"


def demo_counter() -> None:
    c = SimpleCounter()
    print("Start:", c)
    c.inc()
    c.inc(4)
    print("After increments:", c)
    try:
        c.inc(-1)
    except ValueError as e:
        print("Caught error (demonstrating error handling):", e)


def safe_divide(a: float, b: float) -> float | None:
    """Divide a by b and return None on ZeroDivisionError.

    Good small example to show try/except and returning sentinel values.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Small Python tutorial demos")
    parser.add_argument("--demo", choices=["lists", "fib", "primes", "counter", "all"], default="all", help="Which demo to run")
    parser.add_argument("--n", type=int, default=10, help="Number used by some demos (like fib/primes)")
    args = parser.parse_args()

    if args.demo in ("lists", "all"):
        print("\n--- List examples ---")
        list_examples()

    if args.demo in ("fib", "all"):
        print("\n--- Fibonacci (generator) ---")
        show_fibonacci(args.n)

    if args.demo in ("primes", "all"):
        print("\n--- Primes (sieve) ---")
        print(sieve_primes(args.n))

    if args.demo in ("counter", "all"):
        print("\n--- Simple class & error handling ---")
        demo_counter()
        print("safe_divide(10, 2) ->", safe_divide(10, 2))
        print("safe_divide(1, 0) ->", safe_divide(1, 0))


if __name__ == "__main__":
    # Quick smoke assertions used as tiny tests/teaching points
    assert list(sieve_primes(1)) == []
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    main()
