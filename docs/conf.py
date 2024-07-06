"""Sphinx configuration file."""

# pylint: disable=invalid-name

import time
from pathlib import Path

import toml

PYPROJECT = toml.loads(Path(__file__).parent.parent.joinpath("pyproject.toml").read_text(encoding="utf8"))


# General configuration.
author = PYPROJECT["tool"]["poetry"]["authors"][0].split()[0]
copyright = f'{time.strftime("%Y")}, {author}'  # pylint: disable=redefined-builtin  # noqa
html_last_updated_fmt = f"%c {time.tzname[time.localtime().tm_isdst]}"
exclude_patterns = []
extensions = [
    "notfound.extension",  # https://sphinx-notfound-page.readthedocs.io
    "sphinx_copybutton",  # https://sphinx-copybutton.readthedocs.io
    "sphinx_design",  # https://sphinx-design.readthedocs.io
    "sphinx_disqus.disqus",
]
project = PYPROJECT["tool"]["poetry"]["name"]
pygments_style = "sphinx"


# Options for HTML output.
html_copy_source = False
html_theme = "sphinx_rtd_theme"


# https://sphinx-disqus.readthedocs.io
disqus_shortname = "sphinxcontrib-disqus"
