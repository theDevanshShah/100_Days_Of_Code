import pytest

from Day_3 import day3


def test_summarize_numbers_happy_path():
    res = day3.summarize_numbers([1, 2, 3, 4])
    assert res["count"] == 4.0
    assert res["sum"] == 10.0
    assert pytest.approx(res["mean"]) == 2.5
    assert res["min"] == 1.0
    assert res["max"] == 4.0


def test_summarize_numbers_empty_raises():
    with pytest.raises(ValueError):
        day3.summarize_numbers([])
