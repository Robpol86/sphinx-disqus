=======================
Disqus Sphinx Extension
=======================

Add `Disqus <https://disqus.com>`_ comments to your Sphinx documents.

``sphinxcontrib-disqus`` provides a ``disqus`` directive to be used in documents. It automatically adds the Javascript
needed by Disqus. A working example is shown at the bottom of this page.

Project Links
=============

* Documentation: https://sphinxcontrib-disqus.readthedocs.org
* Source code: https://github.com/Robpol86/sphinxcontrib-disqus
* PyPI homepage: https://pypi.python.org/pypi/sphinxcontrib-disqus

Caveats
=======

When generating Sphinx documents locally and browsing to a ``file://`` URL, comments won't load. This is because the
second batch of Javascript code downloaded by Disqus matches the same protocol the browser is using to visit the page
you're on (in this case it's ``file://``). For security reasons Javascript doesn't load from ``file://``, only
``http://`` or ``https://``.

A simple workaround when you're writing docs locally (this isn't an issue once you host your documentation on a web
server or service such as `Read the Docs <https://readthedocs.org/>`_) is to view your HTML files through a simple web
server. You can fire one up easily running these commands (tested on OS X) after building your HTML files:

1. ``cd docs/_build/html``
2. ``python -m SimpleHTTPServer 8080``
3. Browse to http://localhost:8080/

Contents
========

.. toctree::
    :maxdepth: 2

    usage

Comments
========

.. disqus::
    :disqus_identifier: index
