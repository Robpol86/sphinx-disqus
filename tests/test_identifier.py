"""Test disqus_identifier config value scenarios."""

import re

import py
import pytest
from docutils.parsers.rst import directives, roles
from sphinx import application, errors

BASE_CONFIG = """\
import sys
sys.path.append('{}')
extensions = ['sphinxcontrib.disqus']
master_doc = 'index'
nitpicky = True
disqus_shortname = 'good'
"""

PARAMS = [
    ('Some Sample Title', 'Some Sample Title\n=================\n\n', ''),  # Only title has the identifier.
    ('Hi!', '===\nHi!\n===\n\n', ''),  # Another way to specify the title.
    ("&quot;Hmm...&amp;", 'Old Title\n=========\n\n', '    :disqus_identifier: "Hmm...&'),  # Override the title.
    ('The Title', '', '    :disqus_identifier: The Title'),  # No title, option set instead.
    ('', '', ''),  # No identifier set and no title.
]


@pytest.mark.parametrize('expected,rst_title,option', PARAMS)
def test(monkeypatch, tmpdir, expected, rst_title, option):
    """Test valid and invalid values."""
    tmpdir.join('conf.py').write(BASE_CONFIG.format(py.path.local(__file__).join('..', '..')))
    tmpdir.join('conf.py').write('', mode='a')
    tmpdir.join('index.rst').write('{}.. toctree::\n    :maxdepth: 2\n.. disqus::\n{}'.format(rst_title, option))
    monkeypatch.setattr(directives, '_directives', getattr(directives, '_directives').copy())
    monkeypatch.setattr(roles, '_roles', getattr(roles, '_roles').copy())

    srcdir = confdir = str(tmpdir)
    outdir = tmpdir.join('_build', 'html')
    doctreedir = outdir.join('doctrees').ensure(dir=True, rec=True)
    app = application.Sphinx(srcdir, confdir, str(outdir), str(doctreedir), 'html')

    if expected:
        app.builder.build_all()
        html_body = outdir.join('index.html').read()
        disqus_div = re.findall(r'(<div[^>]+ id="disqus_thread"[^>]*></div>)', html_body)[0]
        assert 'data-disqus-identifier="{}"'.format(expected) in disqus_div
        return

    with pytest.raises(errors.SphinxWarning) as exc:
        app.builder.build_all()
    assert 'no title nodes found in document, cannot derive disqus_identifier config value.' == exc.value.args[0]
