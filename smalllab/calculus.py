"""This module contains functions related to calculus.
"""

from collections.abc import Callable

number = int | float

def sign(x: number) -> int:
    """Return -1 if x < 0, 0 if x = 0, 1 if x > 0."""
    return (x > 0) - (x < 0)


def list2poly(L: list[number]) -> Callable[[number], float]:
    """Return a polynomial function with coefficient in L.
    The coefficient of highest-degree term is the first item in list.

    Parameters
    ----------
    L : list of integer or float
    """
    if len(L) == 0:
        raise ValueError("the list cannot be empty")
        
    def p(x: number) -> float:
        deg = len(L) - 1 # the degree of polynomial
        y = 0.0
        for j, coef in enumerate(L):
            y += x**(deg-j) * coef
        return y
    return p


def format_poly(deg: int, coef: number, leading: bool = False) -> str:
    """Return formatted string for a polynomial term.
    
    Parameters
    ----------
    deg : int
        The power of coefficient
    coef : int or float
    leading : bool, default=False
        Whether or not this coefficient is a leading coefficient
    """
    if deg < 0:
        raise ValueError("degree must be nonnegative")

    # If not a zero polynomial, don't display 0
    if coef == 0:
        if leading and deg == 0:
            return '0'
        return ''

    if deg == 0:
        if leading:
            return f"{coef}"
        if coef < 0:
            return f"{coef}"
        return f"+{coef}"

    # Do not show the power if deg = 1
    if deg == 1:
        if leading:
            return f"{coef}x"
        if coef < 0:
            return f"{coef}x"
        return f"+{coef}x"

    # For degree > 1
    if leading:
        return f"{coef}x^{deg}"
    if coef < 0:
        return f"{coef}x^{deg}"
    return f"+{coef}x^{deg}"


def list2polystr(L_: list) -> str:
    """Return a string representing polynomial function with coefficient in L_.
    The coefficient of highest-degree term is the first item in list.

    Parameters
    ----------
    L_ : list of integer or float
    """
    L = L_.copy()
    
    if len(L) == 0:
        return ''
    if len(L) == 1:
        return str(L[0])
    
    deg = len(L) - 1
    L[0] = format_poly(deg, L[0], True)
    for j in range(1, deg+1):
        L[j] = format_poly(deg-j, L[j])

    return ''.join(L)