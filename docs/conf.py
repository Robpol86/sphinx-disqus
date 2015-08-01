import os
import sys
import time

import sphinx_rtd_theme

sys.path.append(os.path.abspath('..'))


# General configuration.
author = 'Robpol86'
exclude_patterns = ['_build']
copyright = '{}, {}'.format(time.strftime('%Y'), author)
extensions = ['sphinxcontrib.disqus']
master_doc = 'index'
nitpicky = True
project = 'sphinxcontrib-disqus'
release = '1.0'
templates_path = ['_templates']
version = release


# Options for HTML output.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = project

# Options for extensions.
disqus_shortname = project
