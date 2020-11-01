Installation
============

Since it is deployed on `PyPI <https://pypi.org/project/libmake/>`_ you can
install simply using ``pip``: ::

   $ pip install libmake

Usage
=====

Write a ``makefile.py`` and run it with: ::

   $ pymake

or for a custom script name ::

   $ pymake -f <filename>

Quick start
-----------

A basic ``makefile.py`` ::

   import shutil

   import libmake
   from libmake import rule_vars as r

   makefile = libmake.Makefile()


   @makefile.add_rule("ciao.html", ["come.md", "va.scss"])
   def test_rule():
       # fp = first_prerequisite
       # t = target
       shutil.copy(str(r.fp), str(r.t))
       print("Ciao, come va?")


   if __name__ == "__main__":
       libmake.run_make(makefile)
