"""Tests for the power function."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import power


def test_power_positive_exponent():
    """Test power with positive exponent."""
    assert power(2, 3) == 8


def test_power_zero_exponent():
    """Test power with zero exponent."""
    assert power(5, 0) == 1
    assert power(-5, 0) == 1


def test_power_one_exponent():
    """Test power with exponent of one."""
    assert power(5, 1) == 5


def test_power_negative_exponent():
    """Test power with negative exponent."""
    result = power(2, -1)
    assert abs(result - 0.5) < 0.0001


def test_power_zero_base():
    """Test power with zero base."""
    assert power(0, 5) == 0


def test_power_square():
    """Test squaring a number."""
    assert power(4, 2) == 16
    assert power(-4, 2) == 16


def test_power_cube():
    """Test cubing a number."""
    assert power(3, 3) == 27
    assert power(-3, 3) == -27
