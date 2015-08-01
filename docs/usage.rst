.. _usage:

=====
Usage
=====

This page documents how to get started with the extension.

Installation
============

Install the extension with pip:

.. code:: bash

    pip install sphinxcontrib-disqus

Configuration
=============

You must specify your site's `shortname <https://help.disqus.com/customer/portal/articles/466208>`_ in your ``conf.py``
along with this extension's name. Here is a sample file with the two things you need to do:

.. code-block:: python

    # General configuration.
    author = 'Your Name Here'
    copyright = '2015, Your Name Here'
    exclude_patterns = ['_build']
    extensions = ['sphinxcontrib.disqus']  # Add to this list.
    master_doc = 'index'
    project = 'my-cool-project'
    release = '1.0'
    version = '1.0'

    # Options for extensions.
    disqus_shortname = 'my-cool-project'  # Add this line to conf.py.

You must include ``sphinxcontrib.disqus`` in ``extensions`` and you must define ``disqus_shortname`` with the shortname
from your Disqus admin page.

Use In Documents
================

There is an additional option you may specify within documents. You have two choices when it comes to specifying the
`identifier <https://help.disqus.com/customer/portal/articles/472099-what-is-a-disqus-identifier->`_:

Automatic
---------

The extension will define the identifier using the document title (first heading in the doc). For this you just specify:

.. code-block:: rst

    .. disqus::

Manual
------

To manually set the identifier for a document using the ``disqus_identifier`` option, specify this instead:

.. code-block:: rst

    .. disqus::
        :disqus_identifier: name_of_this_page
