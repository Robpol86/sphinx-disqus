"""Sphinx extension that embeds Disqus comments in documents.

https://sphinx-disqus.readthedocs.io
https://github.com/Robpol86/sphinx-disqus
https://pypi.org/project/sphinx-disqus
"""
import os
import re
from typing import Dict, List

from docutils import nodes
from docutils.nodes import document
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError, SphinxError

from sphinx_disqus import __version__

RE_SHORTNAME = re.compile("^[a-zA-Z0-9-]{3,50}$")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "_static")


class DisqusError(SphinxError):
    """Non-configuration error. Raised when directive has bad options."""

    category = "Disqus option error"


class DisqusNode(nodes.General, nodes.Element):
    """Disqus <div /> node for Sphinx/docutils."""

    def __init__(self, disqus_shortname: str, disqus_identifier: str):
        """Store directive options during instantiation.

        :param disqus_shortname: Required Disqus forum name identifying the website.
        :param disqus_identifier: Unique identifier for each page where Disqus is present.
        """
        super().__init__()
        self.disqus_shortname = disqus_shortname
        self.disqus_identifier = disqus_identifier

    @staticmethod
    def visit(spht, node):
        """Append opening tags to document body list."""
        html_attrs = {
            "ids": ["disqus_thread"],
            "data-disqus-shortname": node.disqus_shortname,
            "data-disqus-identifier": node.disqus_identifier,
        }
        spht.body.append(spht.starttag(node, "div", "", **html_attrs))

    @staticmethod
    def depart(spht, _):
        """Append closing tags to document body list."""
        spht.body.append("</div>")


class DisqusDirective(Directive):
    """Disqus ".. disqus::" rst directive."""

    option_spec = dict(disqus_identifier=str)

    def get_shortname(self) -> str:
        """Validate and returns disqus_shortname config value.

        :returns: disqus_shortname config value.
        """
        disqus_shortname = self.state.document.settings.env.config.disqus_shortname
        if not disqus_shortname:
            raise ExtensionError("disqus_shortname config value must be set for the disqus extension to work.")
        if not RE_SHORTNAME.match(disqus_shortname):
            raise ExtensionError("disqus_shortname config value must be 3-50 letters, numbers, and hyphens only.")
        return disqus_shortname

    def get_identifier(self) -> str:
        """Validate and returns disqus_identifier option value.

        :returns: disqus_identifier config value.
        """
        if "disqus_identifier" in self.options:
            return self.options["disqus_identifier"]

        title_node = next(iter(self.state.document.traverse(nodes.title)), None)
        if not title_node:
            raise DisqusError("No title nodes found in document, cannot derive disqus_identifier config value.")
        return title_node.astext()

    def run(self) -> List:
        """Executed by Sphinx.

        :returns: Single DisqusNode instance with config values passed as arguments.
        """
        disqus_shortname = self.get_shortname()
        disqus_identifier = self.get_identifier()
        return [DisqusNode(disqus_shortname, disqus_identifier)]


def event_html_page_context(app: Sphinx, pagename: str, templatename: str, context: dict, doctree: document):
    """Called when the HTML builder has created a context dictionary to render a template with.

    Conditionally adding disqus.js to <head /> if the directive is used in a page.

    :param app: Sphinx application object.
    :param pagename: Name of the page being rendered (without .html or any file extension).
    :param templatename: Page name with .html.
    :param context: Jinja2 HTML context.
    :param doctree: Tree of docutils nodes.
    """
    assert app or pagename or templatename  # Unused, for linting.
    if "script_files" in context and doctree and any(hasattr(n, "disqus_shortname") for n in doctree.traverse()):
        # Clone list to prevent leaking into other pages and add disqus.js to this page.
        context["script_files"] = context["script_files"][:] + ["_static/disqus.js"]


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_config_value("disqus_shortname", None, True)
    app.add_directive("disqus", DisqusDirective)
    app.add_node(DisqusNode, html=(DisqusNode.visit, DisqusNode.depart))
    app.connect("builder-inited", lambda app_: app_.config.html_static_path.append(STATIC_DIR))
    app.connect("html-page-context", event_html_page_context)
    return dict(version=__version__)
