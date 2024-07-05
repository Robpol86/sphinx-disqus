.. _install:

============
Installation
============

Getting started is pretty simple. The first step is to install the library.

Once the package is installed add this extension to your Sphinx’s extensions list in the ``conf.py`` file. You'll also need to
define your `Disqus shortname <https://help.disqus.com/en/articles/1717111-what-s-a-shortname>`_ in the same file.

.. code-block:: python

    # conf.py
    extensions = [
         # ... other extensions here
         "sphinx_disqus.disqus",
    ]
    disqus_shortname = "my-cool-project"

The last step is to enable comments on each document.

Specifying an Identifier
========================

By default the extension will define the
`Disqus identifier <https://help.disqus.com/customer/portal/articles/472099-what-is-a-disqus-identifier->`_ using the
document title. To override this behavior you can define your own identifier for a particular document using the
``disqus_identifier`` option.

Comments
========

.. disqus::
