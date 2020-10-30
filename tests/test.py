import subprocess

for arg in ["ciao", "a", None]:
    command = ["python3", "makefile.py"]
    if arg is not None:
        command.append(arg)

    subprocess.run(command)
