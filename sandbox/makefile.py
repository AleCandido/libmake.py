import inspect

import rich
import libmake

makefile = libmake.Makefile()


@makefile.add_rule("*", ["ciao", "come", "va"])
def va():
    rich.get_console().print(
        inspect.cleandoc(
            """[b yellow]I'm supposed to do something[/]

               [i grey54]so I will just print my [u]target[/u]:[/]"""
        ),
        justify="center",
    )

    rich.get_console().print(makefile.target, justify="center")
    rich.get_console().print(
        inspect.cleandoc(
            """
               [i grey54]and my [u]prerequisites[/u]:[/]"""
        ),
        justify="center",
    )
    rich.get_console().print(makefile.prerequisites, justify="center")
    print()


if __name__ == "__main__":
    libmake.run_make(makefile)
