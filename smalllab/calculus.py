"""This module contains functions related to calculus.
"""

number = int | float

def sign(x: number) -> int:
    """Return -1 if x < 0, 0 if x = 0, 1 if x > 0."""
    return (x > 0) - (x < 0)