import subprocess

import rich
import rich.panel
import rich.box

for arg in ["ciao", "a", None]:
    command = ["pymake"]
    if arg is not None:
        command.append(arg)

    rich.print(
        rich.panel.Panel.fit(
            "[magenta] " + " ".join(command) + " [/]",
            title="Running test for",
            box=rich.box.SQUARE,
        )
    )
    subprocess.run(command)
    print()

for arg in ["ciao", None]:
    command = ["pymake", "-f", "makefile_advanced.py"]
    if arg is not None:
        command.append(arg)

    rich.print(
        rich.panel.Panel.fit(
            "[magenta] " + " ".join(command) + " [/]",
            title="Running test for",
            box=rich.box.SQUARE,
        )
    )
    subprocess.run(command)
    print()
