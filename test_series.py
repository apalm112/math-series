# -*- coding: utf-8 -*-
"""Test functions for series.py"""
import pytest


FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (19, 4181),
]


LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    """Test Fibonacci function."""
    from series import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Test Lucas function."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_fib(n, result):
    """Test sum_series without arguements should return Fibonacci."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_sum_series_lucas(n, result):
    """Test sum_series with arguements 2, 1 should return Lucas."""
    from series import sum_series
    assert sum_series(n, 2, 1) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib_iter(n, result):
    """Test Fibonacci function"""
    from series import fib_iter
    assert fib_iter(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_iter(n, result):
    """Test Lucas function."""
    from series import lucas_iter
    assert lucas_iter(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_iter(n, result):
    """Test sum_series without arguements should return Fibonacci."""
    from series import sum_series_iter
    assert sum_series_iter(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_sum_series_iter(n, result):
    """Test sum_series with arguements 2, 1 should return Lucas."""
    from series import sum_series_iter
    assert sum_series_iter(n, 2, 1) == result
