# Contributing

Everyone that wants to contribute to the project should read this document.

## Getting Started

You may follow these steps if you wish to create a pull request. Fork the repo and clone it on your local machine. Then
in the project's directory run this if you're on macOS (requires [Homebrew](https://brew.sh)):

```bash
brew install python@3.7
brew install poetry  # More info: https://python-poetry.org
make clean
POETRY_VIRTUALENVS_IN_PROJECT=true poetry env use "$(brew --prefix)/opt/python@3.7/bin/python3"
```

On Windows:

> TODO

On Ubuntu:

> TODO

On Fedora:

> TODO

Then see if you can run lints and tests:

```bash
make all
```

## Writing Tests

For medium to large changes you'll need to include [tests](./tests) in your pull request. This project uses
[pytest](https://docs.pytest.org/).

## Code Style

Code style must remain consistent in this project. When you're done writing your code you can use
[Black](https://github.com/psf/black) to automatically format Python files:

```bash
poetry run black .
```

Additional code style rules:

1. Write docstrings for all classes, functions, methods, and modules.
1. Document all function/method arguments and return values.
1. Document all class variables instance variables.
1. Documentation guidelines also apply to tests.
1. Avoid `isinstance()` (it breaks [duck typing](https://en.wikipedia.org/wiki/Duck_typing#In_Python)).

## Updating Docs

> TODO

## Thank You!

Thanks for fixing bugs or adding features to the project!
