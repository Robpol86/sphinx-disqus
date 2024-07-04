"""Test extension with regular sphinx-build command."""

from subprocess import CalledProcessError, check_output, STDOUT

import py
import pytest

BASE_CONFIG = """\
import sys
sys.path.append('{}')
nitpicky = True
master_doc = 'index'
extensions = ['sphinx_disqus.disqus']
"""

SHORTNAME_PARAMS = [
    ("disqus_shortname = 'good'", ""),
    ("", "disqus_shortname config value must be set for the disqus extension to work."),
    ("disqus_shortname = ''", "disqus_shortname config value must be set for the disqus extension to work."),
    ("disqus_shortname = 'B@D'", "disqus_shortname config value must be 3-50 letters, numbers, and hyphens only."),
]


@pytest.mark.parametrize("tail,expected_error", SHORTNAME_PARAMS)
def test_shortname(tmpdir: py.path.local, tail: str, expected_error: str):
    """Test working and errors for disqus_shortname configuration.

    :param tmpdir: pytest fixture.
    :param tail: Append to conf.py.
    :param expected_error: Expected error message.
    """
    tmpdir.join("conf.py").write(BASE_CONFIG.format(py.path.local(__file__).join("..", "..")))
    tmpdir.join("conf.py").write(tail, mode="a")
    tmpdir.join("index.rst").write("====\nMain\n====\n\n.. toctree::\n    sub\n.. disqus::")
    tmpdir.join("sub.rst").write(".. _sub:\n\n===\nSub\n===\n\nTest not loading javascript.")

    command = ["sphinx-build", "-W", "-b", "html", ".", "_build/html"]
    if expected_error:
        with pytest.raises(CalledProcessError) as exc:
            check_output(command, cwd=str(tmpdir), stderr=STDOUT)
        error_message = exc.value.output.decode("utf-8")
        assert expected_error in error_message
        return

    stdout = check_output(command, cwd=str(tmpdir), stderr=STDOUT).decode("utf-8")
    assert "warning" not in stdout
    assert tmpdir.join("_build", "html", "_static", "disqus.js").check(file=True)
    body_index = tmpdir.join("_build", "html", "index.html").read()
    assert 'id="disqus_thread"' in body_index
    assert 'data-disqus-identifier="Main"' in body_index
    assert "disqus.js" in body_index
    body_sub = tmpdir.join("_build", "html", "sub.html").read()
    assert 'id="disqus_thread"' not in body_sub
    assert 'data-disqus-identifier="Main"' not in body_sub
    assert "disqus.js" not in body_sub


@pytest.mark.parametrize("rst_title", ["====\nMain\n====\n\n", ""])
def test_identifier(tmpdir: py.path.local, rst_title: str):
    """Test working and errors for disqus_identifier configuration.

    :param tmpdir: pytest fixture.
    :param rst_title: Title of index.rst.
    """
    tmpdir.join("conf.py").write(BASE_CONFIG.format(py.path.local(__file__).join("..", "..")))
    tmpdir.join("conf.py").write("disqus_shortname = 'good'", mode="a")
    tmpdir.join("index.rst").write("{}.. toctree::\n    sub\n.. disqus::".format(rst_title))
    tmpdir.join("sub.rst").write(".. _sub:\n\n===\nSub\n===\n\nTest not loading javascript.")

    command = ["sphinx-build", "-b", "html", ".", "_build/html"]
    if not rst_title:
        with pytest.raises(CalledProcessError) as exc:
            check_output(command, cwd=str(tmpdir), stderr=STDOUT)
        error_message = exc.value.output.decode("utf-8")
        expected_error = "No title nodes found in document, cannot derive disqus_identifier config value."
        assert expected_error in error_message
        return

    stdout = check_output(command, cwd=str(tmpdir), stderr=STDOUT).decode("utf-8")
    assert "warning" not in stdout
    assert tmpdir.join("_build", "html", "_static", "disqus.js").check(file=True)
    body_index = tmpdir.join("_build", "html", "index.html").read()
    assert 'id="disqus_thread"' in body_index
    assert 'data-disqus-identifier="Main"' in body_index
    assert "disqus.js" in body_index
    body_sub = tmpdir.join("_build", "html", "sub.html").read()
    assert 'id="disqus_thread"' not in body_sub
    assert 'data-disqus-identifier="Main"' not in body_sub
    assert "disqus.js" not in body_sub
