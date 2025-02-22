from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray


def matrix_mult(a: NDArray[np.int64], b: NDArray[np.int64]) -> NDArray[np.int64]:
    """Performs matrix multiplication."""
    return np.dot(a, b)


def matrix_power(m: NDArray[np.int64], p: int) -> NDArray[np.int64]:
    """Computes M^p using exponentiation by squaring."""
    result: NDArray[np.int64] = np.eye(len(m), dtype=np.int64)  # Identity matrix
    base: NDArray[np.int64] = m

    while p > 0:
        if p % 2 == 1:  # If p is odd, multiply result by base
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)  # Square the base
        p //= 2  # Reduce exponent by half

    return result


def fibonacci_matrix(n: int) -> Sequence[int]:
    """Computes the nth Fibonacci number using matrix exponentiation."""
    if n <= 0 or n == 1:
        return [0]

    # Fibonacci transformation matrix
    fib_matrix = np.array([[1, 1], [1, 0]], dtype=np.int64)

    sequence = [0, 1]

    for i in range(2, n):
        result = matrix_power(fib_matrix, i - 1)
        sequence.append(int(result[0, 0]))

    return sequence
