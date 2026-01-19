"""Simple calculator module for demonstrating TestRunner."""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a and b

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base raised to the power of exponent
    """
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """Calculate the remainder of a divided by b.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Remainder of a divided by b
    """
    if b == 0:
        raise ValueError("Cannot compute modulo with divisor of zero")
    return a % b
