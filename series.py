# -*- coding: utf-8 -*-
"""This module defines functions that implement mathematical series.

fib(n):

    Returns the nth value in the fibonacci series

>>> fib(2)
1

lucas(n):

    Returns the nth value in the lucas series

>>> lucas(2)
3

sum_series(n)

    Returns the nth value where the first value is optional arguement
    second arguement is the second optional arguement.

>>> sum_series(3)
2
"""


def fib(n):
    """Return nth Fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def lucas(n):
    """Return nth Lucas number."""
    if n <= 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, first=1, second=1):
    """Return either Fibonacci or Lucas series depending on input."""
    if n < 1:
        return 0
    elif n <= 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n - 2, first, second) + sum_series(n - 1, first, second)


if __name__ == '__main__':
    print(__doc__)
