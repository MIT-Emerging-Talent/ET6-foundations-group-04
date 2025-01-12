# Tribonacci Sequence Challenge

## Overview

This challenge involves calculating the nth number in the **Tribonacci sequence**.

- The first three numbers are defined as:
  - T(0) = 0, T(1) = 1, T(2) = 1.
- For n ≥ 3, the sequence is defined as:
  - T(n) = T(n-1) + T(n-2) + T(n-3).

The objective is to write an efficient function to compute the nth Tribonacci number
while handling edge cases and invalid inputs.

---

## Project Contents

### Main Script

The `main.py` file contains the implementation of the `tribonacci` function,
which calculates the nth Tribonacci number.

**Features**:

- Computes the nth Tribonacci number iteratively for optimal performance.
- Handles invalid inputs, such as negative values, by raising a `ValueError`.
- Includes docstrings with detailed explanations and usage examples.

**Example usage**:

```python
>>> from solutions.the_tribonacci_sequence.main import tribonacci
>>> tribonacci(5)
7
>>> tribonacci(10)
149
```

### Unit Tests

The `test_tribonacci.py` file provides a comprehensive suite of tests
for the `tribonacci` function using Python’s built-in `unittest` framework.

### Test Coverage

1. **Base Cases**:
   - Verifies the initial values:
     - T(0) = 0
     - T(1) = 1
     - T(2) = 1

2. **Standard Cases**:
   - Tests for typical Tribonacci calculations, such as:
     - T(5) = 7
     - T(10) = 149

3. **Edge Cases**:
   - Handles larger values of `n`:
     - T(30) = 29249425

4. **Defensive Assertions**:
   - Ensures the function raises a `ValueError` for invalid inputs,
   such as negative values (`n < 0`).

---

## How to Run the Code

### 1. Running the Function

The `tribonacci` function can be imported and executed as follows:

```python
from solutions.the_tribonacci_sequence.main import tribonacci

# Calculate the 7th Tribonacci number
print(tribonacci(7))  # Output: 24
