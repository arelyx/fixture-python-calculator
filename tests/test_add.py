"""Tests for the add function."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import add


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test adding two negative numbers."""
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    """Test adding positive and negative numbers."""
    assert add(-2, 3) == 1
    assert add(2, -3) == -1


def test_add_zero():
    """Test adding with zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_floats():
    """Test adding floating point numbers."""
    result = add(1.5, 2.5)
    assert abs(result - 4.0) < 0.0001


def test_add_large_numbers():
    """Test adding large numbers."""
    assert add(1000000, 2000000) == 3000000
