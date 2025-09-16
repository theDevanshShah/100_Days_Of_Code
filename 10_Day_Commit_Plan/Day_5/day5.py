"""Simple Day 5 utilities.

Provide a small, well-tested example function `fizzbuzz` used in exercises.
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return FizzBuzz sequence from 1 to n inclusive.

    Examples:
        >>> fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result: List[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
