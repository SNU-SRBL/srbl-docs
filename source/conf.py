# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SRBL Docs'
copyright = '2026, Soft Robotics & Bionics Lab'
author = 'Soft Robotics & Bionics Lab'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Keep sidebar expanded even when navigating to other sections
html_context = {
    'display_github': False,
}

# Theme options
html_theme_options = {
    'collapse_navigation': True,  # Keep sidebar expanded
    'sticky_navigation': True,
    'titles_only': True,  # Show only section titles in the sidebar
    'navigation_depth': 4,
}

html_extra_path = ['_static/robots.txt']