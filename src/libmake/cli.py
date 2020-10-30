import pathlib
import subprocess


def pymake():
    makefile = pathlib.Path("makefile.py")

    if makefile.is_file():
        subprocess.run(["python3", str(makefile.absolute())])
    else:
        here = pathlib.Path(".")
        raise ValueError(
            f"'pymake' needs a valid 'makefile.py', no one found at {here.absolute()}"
        )
