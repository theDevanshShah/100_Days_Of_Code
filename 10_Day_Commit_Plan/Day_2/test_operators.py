import math
from Day_2 import operators


def test_arithmetic_examples():
    res = operators.arithmetic_examples(7, 3)
    assert res["add"] == 10
    assert res["div"] == 7 / 3
    assert res["floordiv"] == 7 // 3
    assert res["pow"] == 7 ** 3


def test_comparison_examples():
    res = operators.comparison_examples(5, 5)
    assert res["eq"] is True
    assert res["gte"] is True


def test_logical_examples():
    res = operators.logical_examples(True, False)
    assert res["and"] is False
    assert res["or"] is True


def test_bitwise_examples():
    res = operators.bitwise_examples(6, 2)  # 6 = 0b110, 2 = 0b10
    assert res["and"] == 6 & 2
    assert res["shl"] == 6 << 2


def test_membership_identity_examples():
    seq = [1, 2, 3]
    res = operators.membership_identity_examples(seq, 2, seq, list(seq))
    assert res["in"] is True
    assert res["not_in"] is False
    assert res["is"] is False  # different objects
