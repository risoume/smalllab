"""This module contains functions related to algebra.
"""

from smalllab.nt import gcd

def units(n: int) -> list[int]:
    """Find all natural number a < n where (a, n) = 1."""
    if n < 2:
        raise ValueError("number must be greater than 1")
    return [i for i in range(1, n) if gcd(i, n) == 1]
