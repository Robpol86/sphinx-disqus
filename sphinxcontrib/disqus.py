"""Sphinx extension that embeds Disqus comments in documents.

https://sphinxcontrib-disqus.readthedocs.org
https://github.com/Robpol86/sphinxcontrib-disqus
https://pypi.python.org/pypi/sphinxcontrib-disqus
"""

from __future__ import print_function

import os
import re

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import ExtensionError, SphinxError

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '1.0.0'
RE_SHORTNAME = re.compile('^[a-zA-Z0-9-]{3,50}$')
STATIC_DIR = os.path.join(os.path.dirname(__file__), '_static')


class DisqusError(SphinxError):
    """Non-configuration error. Raised when directive has bad options."""

    category = 'Disqus option error'


class DisqusNode(nodes.General, nodes.Element):
    """Disqus <div /> node for Sphinx/docutils."""

    def __init__(self, disqus_shortname, disqus_identifier):
        """Store directive options during instantiation.

        :param str disqus_shortname: Required Disqus forum name identifying the website.
        :param str disqus_identifier: Unique identifier for each page where Disqus is present.
        """
        super(DisqusNode, self).__init__()
        self.disqus_shortname = disqus_shortname
        self.disqus_identifier = disqus_identifier

    @staticmethod
    def visit(spht, node):
        """Append opening tags to document body list."""
        html_attrs = {
            'ids': ['disqus_thread'],
            'data-disqus-shortname': node.disqus_shortname,
            'data-disqus-identifier': node.disqus_identifier,
        }
        spht.body.append(spht.starttag(node, 'div', '', **html_attrs))

    @staticmethod
    def depart(spht, _):
        """Append closing tags to document body list."""
        spht.body.append('</div>')


class DisqusDirective(Directive):
    """Disqus ".. disqus::" rst directive."""

    optional_arguments = 1
    option_spec = dict(disqus_identifier=str)

    def get_shortname(self):
        """Validate and returns disqus_shortname config value.

        :returns: disqus_shortname config value.
        :rtype: str
        """
        disqus_shortname = self.state.document.settings.env.config.disqus_shortname
        if not disqus_shortname:
            raise ExtensionError('disqus_shortname config value must be set for the disqus extension to work.')
        if not RE_SHORTNAME.match(disqus_shortname):
            raise ExtensionError('disqus_shortname config value must be 3-50 letters, numbers, and hyphens only.')
        return disqus_shortname

    def get_identifier(self):
        """Validate and returns disqus_identifier option value.

        :returns: disqus_identifier config value.
        :rtype: str
        """
        if 'disqus_identifier' in self.options:
            return self.options['disqus_identifier']

        title_nodes = self.state.document.traverse(nodes.title)
        if not title_nodes:
            raise DisqusError('No title nodes found in document, cannot derive disqus_identifier config value.')
        return title_nodes[0].astext()

    def run(self):
        """Executed by Sphinx.

        :returns: Single DisqusNode instance with config values passed as arguments.
        :rtype: list
        """
        disqus_shortname = self.get_shortname()
        disqus_identifier = self.get_identifier()
        return [DisqusNode(disqus_shortname, disqus_identifier)]


class EventHandlers(object):
    """Hold Sphinx event handlers as static methods."""

    @staticmethod
    def insert_javascript(app):
        """Insert Disqus read-only javascript into the document body during the builder-inited event.

        http://sphinx-doc.org/extdev/appapi.html#event-builder-inited
        From: https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/mathjax.py

        :param app: Sphinx application object.
        """
        app.config.html_static_path.append(os.path.relpath(STATIC_DIR, app.confdir))
        app.add_javascript('disqus.js')


def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    :rtype: dict
    """
    app.add_config_value('disqus_shortname', None, True)
    app.add_node(DisqusNode, html=(DisqusNode.visit, DisqusNode.depart))
    app.add_directive('disqus', DisqusDirective)
    app.connect('builder-inited', EventHandlers.insert_javascript)
    return dict(version=__version__)
