import inspect

import rich

import libmake
from libmake import rule_vars as r
from libmake import make_vars as m

makefile = libmake.Makefile()

m.phony << ["ciao"]


@makefile.add_rule("??*", ["ciao", "come", "va"])
def test_rule():
    rich.get_console().print(
        inspect.cleandoc(
            """[b yellow]I'm supposed to do something[/]
               [b red]but I'm advanced![/]

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


if __name__ == "__main__":
    libmake.run_make(makefile)
