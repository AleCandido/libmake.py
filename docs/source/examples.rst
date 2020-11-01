Examples
========

One of the test ``makefile.py`` used in development: ::

   import inspect

   import rich

   import libmake
   from libmake import rule_vars as r

   makefile = libmake.Makefile()


   @makefile.add_rule("a", ["ciao", "come", "va"])
   def test_rule():
       rich.get_console().print(
           inspect.cleandoc(
               """[b yellow]I'm supposed to do something[/]

                  [i grey54]so I will just print my [u]target[/u]:[/]"""
           ),
           justify="center",
       )

       # rich.get_console().print(makefile.target, justify="center")
       rich.get_console().print(r.target, justify="center")
       rich.get_console().print(
           inspect.cleandoc(
               """
                  [i grey54]and my [u]prerequisites[/u]:[/]"""
           ),
           justify="center",
       )
       # rich.get_console().print(makefile.prerequisites, justify="center")
       rich.get_console().print(r.prerequisites, justify="center")
       print()


   @makefile.add_rule("??*")
   def test_rule_vars():
       rich.print("'[yellow]r.t[/]': ", r.t)
       rich.print("'[yellow]r.t()[/]': ", r.t())
       rich.print("'[yellow]r.t().match(\"ciao\")[/]': ", r.t().match("ciao"))
       print()


   if __name__ == "__main__":
       libmake.run_make(makefile)
