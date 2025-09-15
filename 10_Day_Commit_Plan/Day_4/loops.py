"""Simple loop utilities for Day 4.

Functions
- sum_range(start, end): sum integers from start to end inclusive using a for loop.
- first_multiples(n, count): return first `count` multiples of `n` using a for loop.
- repeat_until(predicate, action, max_iters=1000): run `action()` until `predicate()` is True or max iters reached.
"""
from typing import Callable, List


def sum_range(start: int, end: int) -> int:
    """Return the sum of integers from `start` to `end` inclusive.

    Uses a `for` loop to demonstrate iteration over a range.
    If `start` > `end` the function returns 0.
    """
    if start > end:
        return 0
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


def first_multiples(n: int, count: int) -> List[int]:
    """Return a list with the first `count` multiples of `n`.

    Example: `first_multiples(3, 4) -> [3, 6, 9, 12]`.
    If `count` <= 0 returns an empty list.
    """
    if count <= 0:
        return []
    multiples = []
    for i in range(1, count + 1):
        multiples.append(n * i)
    return multiples


def repeat_until(predicate: Callable[[], bool], action: Callable[[], None], max_iters: int = 1000) -> int:
    """Run `action()` until `predicate()` returns True or `max_iters` reached.

    Returns the number of iterations executed. If `predicate()` is True
    before the first action, 0 is returned.
    """
    iters = 0
    while not predicate() and iters < max_iters:
        action()
        iters += 1
    return iters
