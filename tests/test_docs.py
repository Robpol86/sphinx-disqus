"""Make sure documentation builds successfully."""

import os
from subprocess import check_output, STDOUT


def test():
    """Test documentation."""
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    command = ['sphinx-build', '-a', '-E', '-n', '-N', '-W', '-b', 'html', '.', '_build/html']
    check_output(command, cwd=docs_dir, stderr=STDOUT)
