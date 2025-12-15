"""
Half Adder and Full Adder implementations using Boolean algebra.

A Half Adder adds two single-bit binary numbers and produces a sum and carry.
A Full Adder adds three single-bit binary numbers (including carry-in).

Boolean equations:
    Half Adder:
        sum = a XOR b
        carry = a AND b

    Full Adder:
        sum = a XOR b XOR carry_in
        carry = (a AND b) OR (carry_in AND (a XOR b))

Time Complexity: O(1)
Space Complexity: O(1)

Reference: https://en.wikipedia.org/wiki/Adder_(electronics)
"""


def _validate_input(value: int, name: str) -> None:
    """
    Validate that input is 0 or 1.

    >>> _validate_input(0, "a")
    >>> _validate_input(1, "b")
    >>> _validate_input(2, "a")
    Traceback (most recent call last):
        ...
    ValueError: a must be 0 or 1, got 2
    >>> _validate_input(-1, "b")
    Traceback (most recent call last):
        ...
    ValueError: b must be 0 or 1, got -1
    """
    if value not in (0, 1):
        msg = f"{name} must be 0 or 1, got {value}"
        raise ValueError(msg)


def half_adder(a: int, b: int) -> tuple[int, int]:
    """
    Compute the sum and carry of two single-bit binary numbers.

    Args:
        a: First input bit (0 or 1).
        b: Second input bit (0 or 1).

    Returns:
        A tuple (sum, carry) where:
            sum = a XOR b
            carry = a AND b

    >>> half_adder(0, 0)
    (0, 0)
    >>> half_adder(0, 1)
    (1, 0)
    >>> half_adder(1, 0)
    (1, 0)
    >>> half_adder(1, 1)
    (0, 1)
    >>> half_adder(2, 0)
    Traceback (most recent call last):
        ...
    ValueError: a must be 0 or 1, got 2
    >>> half_adder(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: b must be 0 or 1, got -1
    """
    _validate_input(a, "a")
    _validate_input(b, "b")

    # sum = a XOR b
    sum_bit = a ^ b
    # carry = a AND b
    carry = a & b

    return (sum_bit, carry)


def full_adder(a: int, b: int, carry_in: int) -> tuple[int, int]:
    """
    Compute the sum and carry of three single-bit binary numbers.

    Args:
        a: First input bit (0 or 1).
        b: Second input bit (0 or 1).
        carry_in: Carry input bit (0 or 1).

    Returns:
        A tuple (sum, carry) where:
            sum = a XOR b XOR carry_in
            carry = (a AND b) OR (carry_in AND (a XOR b))

    >>> full_adder(0, 0, 0)
    (0, 0)
    >>> full_adder(0, 0, 1)
    (1, 0)
    >>> full_adder(0, 1, 0)
    (1, 0)
    >>> full_adder(0, 1, 1)
    (0, 1)
    >>> full_adder(1, 0, 0)
    (1, 0)
    >>> full_adder(1, 0, 1)
    (0, 1)
    >>> full_adder(1, 1, 0)
    (0, 1)
    >>> full_adder(1, 1, 1)
    (1, 1)
    >>> full_adder(2, 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: a must be 0 or 1, got 2
    >>> full_adder(0, 3, 0)
    Traceback (most recent call last):
        ...
    ValueError: b must be 0 or 1, got 3
    >>> full_adder(0, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: carry_in must be 0 or 1, got -1
    """
    _validate_input(a, "a")
    _validate_input(b, "b")
    _validate_input(carry_in, "carry_in")

    # a XOR b (intermediate result)
    a_xor_b = a ^ b
    # sum = a XOR b XOR carry_in
    sum_bit = a_xor_b ^ carry_in
    # carry = (a AND b) OR (carry_in AND (a XOR b))
    carry = (a & b) | (carry_in & a_xor_b)

    return (sum_bit, carry)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
