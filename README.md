# sphinx-disqus

Embed [Disqus](https://disqus.com) comments in Sphinx documents/pages.

* Python 3.9 through 3.12 supported on Linux, macOS, and Windows.

📖 Full documentation: https://sphinx-disqus.readthedocs.io

[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]
[![PyPI Downloads][pypi-dl-badge]][pypi-dl-link]

[github-ci]: https://github.com/Robpol86/sphinx-disqus/actions/workflows/ci.yml/badge.svg?branch=main
[github-link]: https://github.com/Robpol86/sphinx-disqus/actions/workflows/ci.yml
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
