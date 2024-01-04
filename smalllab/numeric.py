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
    if sign(f(a0)) * sign(f(b0)) > 0:
        raise ValueError("f(a0) and f(b0) must have different signs")

    a, b = a0, b0
    fa, fb = f(a), f(b)

    c = (a + b) / 2
    while b - c > e:
        fc = f(c)
        if sign(fb) * sign(fc) <= 0:
            a, fa = c, fc
        else:
            b, fb = c, fc
        c = (a + b) / 2
    return c


def newton(f: Callable[[number], number], df: Callable[[number], number],
        x0: number, e: number, max_it: int) -> float | None:
    """Find a root of a functin using newton method.

    Parameters
    ----------
    f : Callable
        Function for which the root will be calculated.
    df : Callable
        The derivative of f.
    x0 : int or float
        Initial guess for the root.
    e : int or float
        Error tolerance.
    max_it : int
        Maximum iteration.
    """
    for j in range(1, max_it + 1):
        if df(x0) == 0:
            raise ValueError("the derivative is zero")
            
        x1 = x0 - f(x0) / df(x0)
        error = x1 - x0
        if abs(error) <= e:
            return x1
        x0 = x1
        
    return None


def secant(f: Callable[[number], number], x0: number, x1: number,
        e: number, max_it: int) -> float | None:
    """Find a root of a function using secant method.

    Parameters
    ----------
    f : Callable
        Function for which the root will be calculated.
    x0, x1 : int or float
        Initial guesses for the root.
    e : int or float
        Error tolerance.
    max_it : int
        Maximum iteration.
    """
    fx0 = f(x0)
    for j in range(1, max_it + 1):
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            raise ValueError("f(x1) = f(x0); division by zero")
            
        x2 = x1 - fx1*(x1-x0)/(fx1-fx0)
        error = x2 - x1
        if abs(error) <= e:
            return x2
        
        x0, x1 = x1, x2
        fx0 = fx1
    
    return None