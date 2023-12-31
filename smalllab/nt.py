"""This module contains functions related to number theory.
"""

from math import sqrt, isqrt

number = int | float


def is_square(n: number) -> bool:
    """Check if a number is a perfect square."""
    if n < 0:
        return False        
    if n != int(n):
        return False
    return n == isqrt(int(n)) ** 2


def gcd(a: int, b: int) -> int:
    """Compute the gcd of two integers using Euclidean algorithm."""
    if not ( isinstance(a, int) and isinstance(b, int) ):
        raise ValueError("the arguments must be integers")
    
    while b:
        a, b = b, a % b
    return abs(a)


def is_coprime(a: int, b: int) -> bool:
    """Check if the gcd of two integers is 1."""
    return gcd(a, b) == 1


def is_prime(n: int) -> bool:
    """Check if a number is a prime."""
    if not isinstance(n, int):
        raise TypeError("the argument must be an integer")

    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    j = 5
    root = sqrt(n)
    while j <= root:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
        
    return True


def smallest_prime_factor(n: int) -> int:
    """Find the smallest prime factor of integer greater than 1."""
    if n <= 1:
        raise ValueError("the number must be greater than 1")

    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    j = 5
    root = sqrt(n)
    while j <= root:
        if n % j == 0:
            return j
        if n % (j + 2) == 0:
            return j + 2
        j += 6
        
    return n


def decompose(n: int) -> dict[int, int]:
    """Find the prime factorization of integer greater than 1 as a dictionary,
    with the primes as keys and their exponents as values.
    """
    if n <= 1:
        raise ValueError("the number must be greater than 1")
    
    D = {}
    while n > 1:
        p = smallest_prime_factor(n)
        if p in D.keys():
            D[p] += 1
        else:
            D[p] = 1
        n //= p
    
    return D


def recompose(D: dict[int, int]) -> int:
    """Recover a number from its prime factorization."""
    n = 1
    for p in D.keys():
        n = n * (p ** D[p])
    return n


def divisor_num(n: int) -> int:
    """Find the number of positive divisors of n."""
    if n == 0:
        raise ValueError("the number must be nonzero")

    n = abs(n)
    if n == 1:
        return 1

    sum = 1
    D = decompose(n)
    for p in D.keys():
        sum *= (D[p] + 1)
    return sum


def divisor_sum(n: int) -> int:
    """Find the sum of all positif divisors of n."""
    if n == 0:
        raise ValueError("the number must be nonzero")
    
    n = abs(n)
    if n == 1:
        return 1

    sum = 1
    D = decompose(n)
    for p in D.keys():
        sum *= ((p ** (D[p]+1) - 1) // (p - 1))
    return sum


def is_perfect(n: int) -> bool:
    """Check if the sum of positive divisors of n equals 2*n."""
    return divisor_sum(n) == 2*n


def totient(n: int) -> int:
    """Count the number of positive integers <= n that are coprime to n."""
    if n < 1:
        raise ValueError("the argument must be positive integer")
    if n == 1:
        return 1
    
    sum = 1
    D = decompose(n)
    for p in D.keys():
        sum *= ((p ** (D[p]-1)) * (p - 1))
    return sum


def decimal2binary(n: int) -> str:
    """Return a string consisting digits of binary expansion of n."""
    if not isinstance(n, int):
        raise TypeError("argument must be an integer")
    if n < 0:
        raise ValueError("number must be nonnegative integer")
    if n == 0:
        return "0"

    b = ""
    while n:
        b = str(n % 2) + b
        n //= 2
    return b


def binary2decimal(b: str) -> int:
    """Given a string b of digits of binary expansion,
    returns its decimal representation.
    """
    if not isinstance(b, str):
        raise TypeError("argument must be a string")
    
    n = 0;
    p = len(b)-1
    for j in range(len(b)):
        n += 2**(p-j) * int(b[j])
    return n


def power_mod(a: int, k: int, m: int) -> int:
    """Compute a^k mod m by successive squaring."""
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = b*a % m
        a = a**2 % m
        k //= 2
    return b
