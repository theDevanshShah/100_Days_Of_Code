"""Small utilities for Day 3 exercises.

Provide a tiny, well-typed function that summarizes a list of numbers.
"""
from typing import Iterable, Dict


def summarize_numbers(nums: Iterable[float]) -> Dict[str, float]:
    """Return a small summary for the given numbers.

    The returned dict contains 'count', 'sum', 'mean', 'min', and 'max'.

    Raises ValueError if `nums` is empty.
    """
    nums_list = list(nums)
    if not nums_list:
        raise ValueError("nums must not be empty")

    count = len(nums_list)
    total = sum(nums_list)
    mean = total / count
    return {"count": float(count), "sum": float(total), "mean": float(mean), "min": float(min(nums_list)), "max": float(max(nums_list))}


if __name__ == "__main__":
    print(summarize_numbers([1, 2, 3, 4]))
