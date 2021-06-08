# sphinx-disqus

Embed [Disqus](https://disqus.com) comments in Sphinx documents/pages.

* Python 3.6, 3.7, 3.8, and 3.9 supported on Linux, macOS, and Windows.

📖 Full documentation: TBD

[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]
[![PyPI Downloads][pypi-dl-badge]][pypi-dl-link]

[github-ci]: https://github.com/Robpol86/sphinx-disqus/workflows/ci/badge.svg?branch=main
[github-link]: https://github.com/Robpol86/sphinx-disqus
[codecov-badge]: https://codecov.io/gh/Robpol86/sphinx-disqus/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/Robpol86/sphinx-disqus
[rtd-badge]: https://readthedocs.org/projects/sphinx-disqus/badge/?version=latest
[rtd-link]: https://sphinx-disqus.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
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
extensions = ["sphinx_disqus.disqus"]
disqus_shortname = "my-cool-project"
```

Also add this to any document you wish to have comments:

```rst
.. disqus::
```

## TODO

1. publish (then delete, new package name anyway)
1. other todos in README.

* drop google analytics from docs
* include LICENSE in package
* https://github.com/search?q=%22tool.pylint%22+similarities&type=Code
* https://docs.pytest.org/en/6.2.x/customize.html#pyproject-toml
* test external PR
* readthedocs theme and hosting, no github pages
* delete gh-pages branch
* unignore docs/ linting
* s/README.rst/README.md/
* more tool.poetry.urls
* Update gh repo link to rtd docs.
* Explore gh Packages section.
* revisit classifiers
* revisit linting/test ignores/skips
* https://www.python.org/dev/peps/pep-0423/#how-to-rename-a-project
* Move CHANGELOG validation out of pytest and into gh workflow (like black does)
* Redo docstrings and args with type hints.
* Integration test with no dev dependencies
