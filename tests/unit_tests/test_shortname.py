"""Test disqus_shortname config value scenarios."""

import re

import py
import pytest
from _pytest.monkeypatch import MonkeyPatch
from docutils.parsers.rst import directives, roles
from sphinx import application, errors

BASE_CONFIG = """\
import sys
sys.path.append('{}')
extensions = ['sphinx_disqus.disqus']
master_doc = 'index'
nitpicky = True
"""

PARAMS = [
    ("disqus_shortname = 'good'", ""),
    ("", "disqus_shortname config value must be set for the disqus extension to work."),
    ("disqus_shortname = ''", "disqus_shortname config value must be set for the disqus extension to work."),
    ("disqus_shortname = 'B@D'", "disqus_shortname config value must be 3-50 letters, numbers, and hyphens only."),
]


@pytest.mark.parametrize("tail,expected_error", PARAMS)
def test(monkeypatch: MonkeyPatch, tmpdir: py.path.local, tail: str, expected_error: str):
    """Test valid and invalid values."""
    tmpdir.join("conf.py").write(BASE_CONFIG.format(py.path.local(__file__).join("..", "..")))
    tmpdir.join("conf.py").write(tail, mode="a")
    tmpdir.join("index.rst").write("====\nMain\n====\n\n.. toctree::\n    :maxdepth: 2\n.. disqus::")
    monkeypatch.setattr(directives, "_directives", getattr(directives, "_directives").copy())
    monkeypatch.setattr(roles, "_roles", getattr(roles, "_roles").copy())

    srcdir = confdir = str(tmpdir)
    outdir = tmpdir.join("_build", "html")
    doctreedir = outdir.join("doctrees").ensure(dir=True, rec=True)
    app = application.Sphinx(srcdir, confdir, str(outdir), str(doctreedir), "html")

    if not expected_error:
        app.builder.build_all()
        html_body = outdir.join("index.html").read()
        disqus_div = re.findall(r'(<div[^>]+ id="disqus_thread"[^>]*></div>)', html_body)[0]
        assert 'data-disqus-shortname="good"' in disqus_div
        return

    with pytest.raises(errors.ExtensionError) as exc:
        app.builder.build_all()
    assert expected_error == exc.value.args[0]
