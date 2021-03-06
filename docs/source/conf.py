# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

# sys.path.insert(0, os.path.abspath("../../src/"))

import libmake.version

# -- Project information -----------------------------------------------------

project = "libmake.py"
copyright = "2020, Alessandro Candido"
author = "Alessandro Candido"

# The short X.Y version
version = libmake.version.short_version
# The full version, including alpha/beta/rc tags
release = libmake.version.full_version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Application API  --------------------------------------------------------

# Further info at: https://www.sphinx-doc.org/en/master/extdev/appapi.html


def run_apidoc(_):
    from sphinx.ext.apidoc import main
    import pathlib
    import sys

    docs_source = pathlib.Path(__file__).parent.absolute()
    project_root = docs_source.parents[1]
    sys.path.append(str(project_root / "src"))
    module = project_root / "src"
    main(
        [
            "--no-toc",
            "--module-first",
            "--separate",
            "--ext-todo",
            "--ext-mathjax",
            "--ext-coverage",
            "--templatedir",
            str(docs_source / "_templates"),
            "--output-dir",
            str(docs_source / "modules"),
            str(module),
        ]
    )


def setup(app):
    app.connect("builder-inited", run_apidoc)
