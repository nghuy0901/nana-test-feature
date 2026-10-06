# Nana feature acceptance fixture

Public synthetic code only. No private source, credentials or production data.

The complete baseline exposes `calculator.double(value)` and has a passing regression. The separate approved feature workflow will add `calculator.triple(value)` and its behavior check; the seed contains no stub for that feature.

Run locally:

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
```

GitHub Actions runs `feature-pr` for pull requests and `feature-main` for pushes to main. Implementation of the requested feature must wait for genuine revision-bound approval.
