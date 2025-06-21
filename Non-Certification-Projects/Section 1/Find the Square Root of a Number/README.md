# Bisection Method: Square Root Approximation (Python)

This project implements the **bisection method** to approximate the square root of a non-negative number using pure Python. It’s a clear and methodical demonstration of numerical methods applied in scientific computing, designed to reinforce concepts from freeCodeCamp’s Scientific Computing with Python curriculum.

---

## What It Does

Given a non-negative number, the program:
- Checks for special cases (0 and 1)
- Uses the bisection method to repeatedly narrow down a guess interval
- Compares square differences using an absolute tolerance
- Returns an estimated square root with high precision

---

## What I Practiced

### Mathematical Concepts
- Numerical approximation of roots
- Tolerance-based stopping criteria
- Midpoint averaging for convergence

### Python Skills
- Control flow with `if`, `elif`, `else`
- `for` loop with dummy variable `_`
- Floating point comparison using `abs()`
- Custom error handling with `raise ValueError`

---

## Sample Output

```python
The square root of 16 is approximately 4.0
```

---

## Function Overview

```
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Approximates the square root of a number using the bisection method
```
- square_target: number to find the square root of (must be ≥ 0)
- tolerance: how close the square of the guess must be to the target
- max_iterations: maximum number of guesses before stopping

---

## Tech Stack
Language: Python 3.x

No external dependencies required

---

## Why This Project Matters
Bisection is a root-finding algorithm and lays a foundation for more 
complex numerical techniques like Newton-Raphson. This project showcases how basic math 
and logic can produce accurate and elegant solutions.