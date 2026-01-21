"""Tests for the divide function."""

import sys
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import divide


def test_divide_positive_numbers():
    """Test dividing two positive numbers."""
    assert divide(10, 2) == 5


def test_divide_negative_numbers():
    """Test dividing two negative numbers."""
    assert divide(-10, -2) == 5


def test_divide_mixed_numbers():
    """Test dividing positive and negative numbers."""
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5


def test_divide_by_one():
    """Test dividing by one."""
    assert divide(5, 1) == 5
    assert divide(-5, 1) == -5


def test_divide_zero_numerator():
    """Test dividing zero by a number."""
    assert divide(0, 5) == 0


def test_divide_floats():
    """Test dividing floating point numbers."""
    result = divide(7.5, 2.5)
    assert abs(result - 3.0) < 0.0001


def test_divide_by_zero():
    """Test dividing by zero should raise ValueError.
    
    The divide function should raise ValueError when attempting
    to divide by zero, similar to the modulo function.
    """
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_fractional_result():
    """Test division that results in a fraction."""
    result = divide(5, 2)
    assert abs(result - 2.5) < 0.0001
