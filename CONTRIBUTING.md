# Contributing

Everyone that wants to contribute to the project should read this document.

## Getting Started

You may follow these steps if you wish to create a pull request. Fork the repo and clone it on your local machine. Then
in the project's directory run this if you're on macOS (requires [Homebrew](https://brew.sh)):

```bash
brew install python
brew install poetry  # More info: https://python-poetry.org
make clean
```

On Ubuntu (including Windows WSL2):

```bash
sudo apt-get update && sudo apt-get install make python3-virtualenv python3
curl -sSL https://install.python-poetry.org | python3 -
make clean
```

Then see if you can run lints and tests:

```bash
make deps all
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

If you're adding a new feature you'll need to update the [Sphinx](http://sphinx-doc.org/) documentation for this project.
Docs are located in the [docs](./docs) directory and can be written using
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) or
[Markdown](https://myst-parser.readthedocs.io/en/latest/using/syntax.html).

To locally build docs and view them in a browser you can run:

```bash
make docs
```

Then browse to: `docs/_build/html/index.html`

## Thank You!

Thanks for fixing bugs or adding features to the project!
