import typer

from cs_notes_and_code.code.fibonacci.compute_types import ComputeType
from cs_notes_and_code.code.fibonacci.generator import fibonacci_generator
from cs_notes_and_code.code.fibonacci.list_comprehension import fibonacci_full_sequence
from cs_notes_and_code.code.fibonacci.matrix import fibonacci_matrix
from cs_notes_and_code.code.fibonacci.naive import compute_fibonacci_naive
from cs_notes_and_code.code.fibonacci.recursive import compute_fibonacci_recursive


def _run_fibonacci(
    n: int = typer.Option(...), compute_type: ComputeType = ComputeType.NAIVE
) -> None:
    match compute_type:
        case ComputeType.NAIVE:
            print(compute_fibonacci_naive(n))  # noqa: T201
        case ComputeType.RECURSIVE:
            print(compute_fibonacci_recursive(n))  # noqa: T201
        case ComputeType.MATRIX:
            print(fibonacci_matrix(n))  # noqa: T201
        case ComputeType.GENERATOR:
            print(list(fibonacci_generator(n)))  # noqa: T201
        case ComputeType.LIST:
            print(fibonacci_full_sequence(n))  # noqa: T201


def main() -> None:
    return typer.run(_run_fibonacci)


if __name__ == "__main__":
    main()
