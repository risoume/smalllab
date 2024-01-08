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


def lagrange(X: list[number], Y: list[number], xp: number) -> float:
    """Given data points X and Y, and a value xp,
    evaluate Pn(xp) where Pn is the Lagrange's polynomial.

    Parameters
    ----------
    X, Y : list of int or float
        All values in X must be distinct.
        The length of X and Y must be equal and greater than 1.
    xp : int or float
    """
    if len(X) != len(Y):
        raise ValueError("the length of X and Y must be equal")
    if len(X) < 2:
        raise ValueError("the length of X and Y must be greater than 1")
    if len(set(X)) != len(X):
        raise ValueError("all values in X must be distinct")
    
    n = len(X)
    yp = 0.0
    for j in range(n):
        p = 1.0
        for k in range(n):
            if j != k:
                p *= (xp-X[k]) / (X[j]-X[k])
        yp += Y[j] * p
    return yp


def divdif(X: list[number], Y: list[number]) -> list[float]:
    """Calculate the set of divided differences
    f[x0,x1], f[x0,x1,x2], ..., f[x0,x1,...,xn].
    
    Parameters
    ----------
    X, Y : list of int or float
        All entries in X must be distinct.
        The length of X and Y must be equal and greater than 1.
    """
    if len(X) != len(Y):
        raise ValueError("the length of X and Y must be equal")
    if len(X) < 2:
        raise ValueError("the length of X and Y must be greater than 1")
    if len(set(X)) != len(X):
        raise ValueError("all values in X must be distinct")
        
    n = len(X)
    D = Y.copy()
    for j in range(1, n):
        for k in range(j, n):
            D[k] = (D[k]-D[j-1]) / (X[k]-X[j-1])
    return D


def newton_divdif(X: list[number], Y: list[number], xp: number) -> float:
    """Evaluate the Newton divided difference at xp."""
    n = len(X) - 1
    D = divdif(X, Y)
    p = D[n]
    for j in range(1, n+1):
        p = D[n-j] + (xp-X[n-j])*p
    return p


def near_minimax(f: Callable[[number], number], n: int) -> Callable:
    """Construct the near minimax approximation of degree n
    for a given function f on [-1,1] using newton divided difference.
    """
    from smalllab.calculus import chebyshev_zeros
    
    nodes = chebyshev_zeros(n+1)
    y_values = [f(x) for x in nodes]
    def near_minimax_(xp):
        return newton_divdif(nodes, y_values, xp)
    return near_minimax_


def trapezoidal(f: Callable, a: number, b: number, n: int) -> float:
    """Evaluate the integral of f over [a, b] using trapezoidal rule
    with n subdivision.
    """
    if a > b:
        raise ValueError("a must be less than b")
    if n < 1:
        raise ValueError("n must be positive integer")
    
    h = (b-a) / n
    sum = (f(a) + f(b)) / 2
    for j in range(1, n):
        sum += f(a+j*h)
    return sum * h