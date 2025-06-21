def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Estimate the square root of a non-negative number using the bisection method.

    Args:
        square_target (float): The number to compute the square root of.
        tolerance (float): Acceptable error margin between guess^2 and square_target.
        max_iterations (int): Maximum number of bisection steps to attempt.

    Returns:
        float or None: Approximated square root, or None if it fails to converge.
    """
    # Handle special cases: negative input is invalid; 0 and 1 have known roots
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize search bounds
        low = 0
        high = max(1, square_target)
        root = None

        # Perform iterative bisection
        for _ in range(max_iterations):
            mid = (low + high) / 2          # Compute midpoint of interval
            square_mid = mid ** 2           # Square the midpoint

            # Check if current guess is within tolerance
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break  # Stop if good enough

            # Narrow the interval based on whether guess is too low or too high
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        # Report outcome
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')

    return root


# Example usage: estimate the square root of 16
N = 16
square_root_bisection(N)
