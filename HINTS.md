# Calculator Project Hints

## Project Overview

A simple calculator module that provides basic arithmetic operations.
Designed to demonstrate TestRunner's capabilities.

## Architecture

- `src/calculator.py` - Main calculator functions
- `tests/` - Pytest test files, one per function

## Test Coverage

Each arithmetic operation has its own test file:
- `test_add.py` - Tests for addition
- `test_subtract.py` - Tests for subtraction
- `test_multiply.py` - Tests for multiplication
- `test_divide.py` - Tests for division
- `test_power.py` - Tests for exponentiation

## Critical Paths

Changes to `calculator.py` will likely affect all test files.
Pay special attention to error handling in divide and modulo functions.

## Expected Behavior

When running TestRunner:
1. Tests related to modified functions should be flagged as high-risk
2. The LLM should identify which tests are most likely to fail based on changes
