# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Scorpionz'
copyright = '2025, Scorionz - 26254'
author = 'Scorionz - 26254'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
]

pygments_style = "friendly"
pygments_dark_style = "native"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ar'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_logo = "_static/logo.jpg"
html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#6a5acd",    # brand
        "color-brand-content": "#2563eb",    # links
    },
    "dark_css_variables": {
        "color-brand-primary": "#8b7bff",
        "color-brand-content": "#93c5fd",
    },
}
html_static_path = ['_static']

def setup(app):
    app.add_css_file("rtl.css")