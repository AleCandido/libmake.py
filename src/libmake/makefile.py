import rich
import rich.align
import rich.style

from .rule import Rule


class Makefile:
    def __init__(self):
        self.rules = []

    def add_rule(self, target, prerequisites, recipe):
        self.rules.append(Rule(target, prerequisites, recipe))

    def get_rule(self, target):
        pass

    def run(self, *args):
        import inspect

        rich.get_console().print(
            inspect.cleandoc(
                """[b yellow]I'm supposed to do something[/]

                [i grey54]so I will just print my input:[/]"""
            ),
            justify="center",
        )

        rich.get_console().print(args, justify="center")
