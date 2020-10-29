import libmake

makefile = libmake.Makefile()

makefile.add_rule("ciao", "come", "va")

if __name__ == "__main__":
    libmake.run_make(makefile)
