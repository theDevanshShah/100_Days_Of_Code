"""Small examples demonstrating Python operators.

Functions are tiny and pure so they can be imported and tested.
"""

def arithmetic_examples(a: int, b: int) -> dict:
    """Return arithmetic operations between a and b."""
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b,
        "floordiv": a // b,
        "mod": a % b,
        "pow": a ** b,
    }


def comparison_examples(a, b) -> dict:
    return {
        "eq": a == b,
        "neq": a != b,
        "gt": a > b,
        "lt": a < b,
        "gte": a >= b,
        "lte": a <= b,
    }


def logical_examples(x: bool, y: bool) -> dict:
    return {"and": x and y, "or": x or y, "not_x": not x}


def bitwise_examples(x: int, y: int) -> dict:
    return {"and": x & y, "or": x | y, "xor": x ^ y, "shl": x << y, "shr": x >> y}


def membership_identity_examples(seq, item, a, b) -> dict:
    return {
        "in": item in seq,
        "not_in": item not in seq,
        "is": a is b,
        "is_not": a is not b,
    }


if __name__ == "__main__":
    print("Arithmetic:", arithmetic_examples(7, 3))
    print("Comparison:", comparison_examples(7, 3))
    print("Logical:", logical_examples(True, False))
    print("Bitwise:", bitwise_examples(6, 2))
    print("Membership/Identity:", membership_identity_examples([1, 2, 3], 2, [], []))
