# ci-pipeline-lab

A small Python project for learning continuous integration. It converts temperatures between Celsius and Fahrenheit, checks the code with Ruff, and tests it with pytest.

## Run the same checks that CI runs

Install [uv](https://docs.astral.sh/uv/), then from this folder run:

```powershell
uv sync --locked
uv run ruff check .
uv run pytest -v
```

GitHub Actions runs those same commands on every push to a branch other than `main`, and on every pull request into `main`. The workflow file is `.github/workflows/ci.yml`.
