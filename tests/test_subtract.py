"""Tests for the subtract function."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import subtract


def test_subtract_positive_numbers():
    """Test subtracting two positive numbers."""
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    """Test subtracting two negative numbers."""
    assert subtract(-5, -3) == -2


def test_subtract_mixed_numbers():
    """Test subtracting positive and negative numbers."""
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8


def test_subtract_zero():
    """Test subtracting with zero."""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0


def test_subtract_same_numbers():
    """Test subtracting same numbers."""
    assert subtract(5, 5) == 0
    assert subtract(-5, -5) == 0


def test_subtract_floats():
    """Test subtracting floating point numbers."""
    result = subtract(5.5, 2.5)
    assert abs(result - 3.0) < 0.0001
