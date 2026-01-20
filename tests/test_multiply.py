"""Tests for the multiply function."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import multiply


def test_multiply_positive_numbers():
    """Test multiplying two positive numbers."""
    assert multiply(3, 4) == 12


def test_multiply_negative_numbers():
    """Test multiplying two negative numbers."""
    assert multiply(-3, -4) == 12


def test_multiply_mixed_numbers():
    """Test multiplying positive and negative numbers."""
    assert multiply(-3, 4) == -12
    assert multiply(3, -4) == -12


def test_multiply_by_zero():
    """Test multiplying by zero."""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0


def test_multiply_by_one():
    """Test multiplying by one."""
    assert multiply(5, 1) == 5
    assert multiply(1, 5) == 5


def test_multiply_floats():
    """Test multiplying floating point numbers."""
    result = multiply(2.5, 4.0)
    assert abs(result - 10.0) < 0.0001
