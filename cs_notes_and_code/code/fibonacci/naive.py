from collections.abc import Sequence


def compute_fibonacci_naive(n: int) -> Sequence[int]:
    fibonacci_series = [0, 1]
    i = 1
    while len(fibonacci_series) < n:
        i += 1
        fibonacci_series.append(fibonacci_series[i - 1] + fibonacci_series[i - 2])

    return fibonacci_series
