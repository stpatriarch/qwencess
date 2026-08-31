# Configuration file for the Sphinx documentation builder. For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))


project = 'Nerdnote'
copyright = '2026, stpatriarch'
author = 'stpatriarch'
release = '0.0.1a20260101'

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = ".rst"

autodoc_member_order = "bysource"

autodoc_typehints = "description"

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}


templates_path = ['_templates']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**/drafts/*',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
