import pytest
import importlib.util
from pathlib import Path

# Load module by file path because the package directory starts with a digit
spec = importlib.util.spec_from_file_location(
    "day5", Path(__file__).parent / "day5.py"
)
day5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day5)  # type: ignore
fizzbuzz = day5.fizzbuzz


def test_fizzbuzz_basic():
    assert fizzbuzz(1) == ["1"]
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert fizzbuzz(5)[-1] == "Buzz"


def test_fizzbuzz_15():
    seq = fizzbuzz(15)
    assert seq[2] == "Fizz"
    assert seq[4] == "Buzz"
    assert seq[14] == "FizzBuzz"


def test_negative_raises():
    with pytest.raises(ValueError):
        fizzbuzz(-1)
