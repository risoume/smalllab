"""This module contains functions related to numerical methods.
"""

from collections.abc import Callable
from smalllab.calculus import sign

number = int | float

def bisect(f: Callable[[number], number], a0: number, b0: number, e: number) -> float:
    """Find a root of f on [a0, b0] with error tolerance e
    using bisection method.
    """
    if a0 >= b0:
        raise ValueError("a0 must be less than b0")
    if e <= 0:
        raise ValueError("error tolerance must be positive")

    a, b = a0, b0
    fa, fb = f(a), f(b)

    if sign(fa) * sign(fb) > 0:
        raise ValueError("f(a0) and f(b0) must have different signs")

    c = (a + b) / 2
    while b - c > e:
        fc = f(c)
        if sign(fb) * sign(fc) <= 0:
            a, fa = c, fc
        else:
            b, fb = c, fc
        c = (a + b) / 2
    return c