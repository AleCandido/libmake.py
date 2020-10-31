import pathlib
import shutil

import rich

import libmake
from libmake import rule_vars as r

makefile = libmake.Makefile()


@makefile.add_rule("ciao.txt", "come.txt")
def test_rule():
    src = pathlib.Path(str(r.p)).absolute()
    dst = pathlib.Path(str(r.t)).absolute()
    shutil.copy(src, dst)
    print(f"Copied {r.p} to {r.t}")


if __name__ == "__main__":
    libmake.run_make(makefile)
