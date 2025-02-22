def compute_fibonacci_recursive(
    n: int, sequence: list[int] | None = None  # noqa: FA102
) -> list[int]:
    if sequence is None:
        sequence = [0, 1]
    if len(sequence) >= n:
        return sequence[:n]
    sequence.append(sequence[-1] + sequence[-2])
    return compute_fibonacci_recursive(n, sequence)
