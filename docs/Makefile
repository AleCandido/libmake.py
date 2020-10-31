# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXAPI     ?= sphinx-apidoc
SOURCEDIR     = source
BUILDDIR      = build

PKGSRC        = ../src/

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile modules all modclean cleanall

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@if [ $@ != "clean" ]; then \
		$(SPHINXAPI) --no-toc --module-first --separate \
			--ext-todo --ext-mathjax --ext-coverage \
			-t source/_templates -o "$(SOURCEDIR)/modules" $(PKGSRC); \
	else \
		echo "Removing 'source/modules'..."; \
		rm -rf source/modules; \
	fi
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
