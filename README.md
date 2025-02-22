# cs-notes-and-code

Practical exercises and structured notes covering computer science topics.

## Set up

```
brew install pre-commit poetry
poetry self add poetry-plugin-shell
poetry sync
poetry shell
```

## Code exercises

### Compute fibonacci sequence

```
python -m cs_notes_and_code.code.fibonacci.run_fibonacci --n <LENGTH_OF_SEQUENCE> --compute-type <COMPUTE_TYPE>
```

where `<LENGTH_OF_SEQUENCE>` can be any positive integer and `<COMPUTE_TYPE>` can take any of the following values:

```
- "naive"
- "generator"
- "recursive"
- "matrix"
- "list"
```
