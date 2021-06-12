"""PROJECT RENAMED TO sphinx-disqus"""
import warnings

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '1.1.1'

warnings.warn("sphinxcontrib-disqus is deprecated, use sphinx-disqus instead", DeprecationWarning)

from sphinx_disqus.disqus import *  # noqa
