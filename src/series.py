# -*- coding: utf-8 -*-
"""This module defines functions that implement mathematical series.

fibonacci(n):

    Returns the nth value in the fibonacci series using recursion.

>>> fibonacci(2)
1

lucas(n):

    Returns the nth value in the lucas series using recursion.

>>> lucas(2)
3

sum_series(n)

    Returns the nth value using recursion, where the first value is optional argument,
    second argument is the second optional argument.

>>> sum_series(3)
2

fibonacci_iter(n)

    Returns the nth value in the fibonacci series using iteration.

>>> fibonacci_iter(2)
1

lucas_iter(n):

Returns the nth value in the lucas series using iteration.

>>> lucas_iter(2)
3

sum_series_iter(n)

Returns the nth value using iteration, where the first value is optional argument,
second argument is the second optional argument.

>>> sum_series_iter(3)
2
"""


def fibonacci(n):
    """Return nth Fibonacci number."""
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """Return nth Lucas number."""
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, first=0, second=1):
    """Return either Fibonacci or Lucas series depending on input."""
    if n < 1:
        return first
    elif n <= 1:
        return second
    else:
        return sum_series(n - 2, first, second) + sum_series(n - 1, first, second)


def fibonacci_iter(n):
    """Return nth Fibonacci number via iteration."""
    fibonacci = [0, 1]
    for num in range(2, n + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[n]


def lucas_iter(n):
    """Return nth lucas number via iteration."""
    lucas = [2, 1]
    for num in range(2, n + 1):
        lucas.append(lucas[-1] + lucas[-2])
    return lucas[n]


def sum_series_iter(n, first=0, second=1):
    """Return either Fibonacci or Lucas series by iteration depending on input."""
    lucas = [first, second]
    for num in range(2, n + 1):
        lucas.append(lucas[-1] + lucas[-2])
    return lucas[n]


if __name__ == '__main__':
    print(__doc__)
