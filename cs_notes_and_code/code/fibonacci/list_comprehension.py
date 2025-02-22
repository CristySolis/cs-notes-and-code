def fibonacci_full_sequence(n: int) -> list[int]:
    """Generates the Fibonacci sequence up to the nth term."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:  # noqa: PLR2004
        return [0, 1]

    sequence: list[int] = [0, 1]
    a: int = 0
    b: int = 1

    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)

    return sequence
