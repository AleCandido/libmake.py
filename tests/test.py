import subprocess

import rich
import rich.panel
import rich.box

for arg in ["ciao", "a", None]:
    command = ["python3", "makefile.py"]
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
