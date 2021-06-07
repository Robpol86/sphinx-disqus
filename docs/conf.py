"""Sphinx configuration file."""

import os
import time
from subprocess import check_output

SETUP = os.path.join(os.path.dirname(__file__), "..", "setup.py")


# General configuration.
author = check_output([SETUP, "--author"]).strip().decode("ascii")
copyright = "{}, {}".format(time.strftime("%Y"), author)  # noqa
master_doc = "index"
project = check_output([SETUP, "--name"]).strip().decode("ascii")
pygments_style = "friendly"
release = version = check_output([SETUP, "--version"]).strip().decode("ascii")
templates_path = ["_templates"]
extensions = list()


# Options for HTML output.
html_context = dict(
    conf_py_path="/docs/",
    display_github=True,
    github_repo=os.environ.get("TRAVIS_REPO_SLUG", "/" + project).split("/", 1)[1],
    github_user=os.environ.get("TRAVIS_REPO_SLUG", "robpol86/").split("/", 1)[0],
    github_version=os.environ.get("TRAVIS_BRANCH", "master"),
    source_suffix=".rst",
)
html_copy_source = False
html_favicon = "favicon.ico"
html_theme = "sphinx_rtd_theme"
html_title = project


# disqus
extensions.append("sphinxcontrib.disqus")
disqus_shortname = project


# google analytics
extensions.append("sphinxcontrib.googleanalytics")
googleanalytics_id = "UA-82627369-1"

# SCVersioning.
scv_banner_greatest_tag = True
scv_grm_exclude = (".gitignore", ".nojekyll", "README.rst")
scv_show_banner = True
scv_sort = ("semver", "time")
