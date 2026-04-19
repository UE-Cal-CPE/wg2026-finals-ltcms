# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'LeanTech Knowledge Hub'
copyright = '2026, LeanTech IT Solutions, Inc.'
author = 'LeanTech IT Solutions, Inc.'

release = '0.1'
version = '1.6.2'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme_options = {
    'prev_next_buttons_location': None
}
html_show_sourcelink = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
