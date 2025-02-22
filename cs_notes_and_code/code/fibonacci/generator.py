from collections.abc import Iterator


def fibonacci_generator(n: int) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
