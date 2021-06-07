# sphinx-disqus

Embed [Disqus](https://disqus.com) comments in Sphinx documents/pages.

* Python 3.6, 3.7, 3.8, and 3.9 supported on Linux, macOS, and Windows.

📖 Full documentation: TBD

[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![PyPI][pypi-badge]][pypi-link]
[![PyPI Downloads][pypi-dl-badge]][pypi-dl-link]

[github-ci]: https://github.com/Robpol86/sphinx-disqus/workflows/ci/badge.svg?branch=main
[github-link]: https://github.com/Robpol86/sphinx-disqus
[codecov-badge]: https://codecov.io/gh/Robpol86/sphinx-disqus/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/Robpol86/sphinx-disqus
[rtd-badge]: https://readthedocs.org/projects/sphinx-disqus/badge/?version=latest
[rtd-link]: https://sphinx-disqus.readthedocs.io/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-disqus.svg
[pypi-link]: https://pypi.org/project/sphinx-disqus
[pypi-dl-badge]: https://img.shields.io/pypi/dw/sphinx-disqus?label=pypi%20downloads
[pypi-dl-link]: https://pypistats.org/packages/sphinx-disqus

## Quickstart

To install run the following:

```bash
pip install sphinx-disqus
```

To use in Sphinx simply add to your `conf.py`:

```python
extensions = ["sphinx_disqus"]
disqus_shortname = "my-cool-project"
```

Also add this to any document you wish to have comments:

```rst
.. disqus::
```

## Local Development

This project runs on Python 3 and relies on [Python Poetry](https://python-poetry.org).

To develop on macOS use [Homebrew](https://brew.sh):

```bash
brew install python@3.7
brew install poetry
make clean
POETRY_VIRTUALENVS_IN_PROJECT=true poetry env use "$(brew --prefix)/opt/python@3.7/bin/python3"
```

Then see if you can run lints and tests:

```bash
make lint
make test
make it
```
