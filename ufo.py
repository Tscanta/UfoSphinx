# ==========================================
# UFOSPHINX CLI
#
# This file is what the user runs.
#
# Example:
#
# py ufo.py run examples/hello.ufo
# ==========================================

import subprocess
import sys

from compiler.compiler import Compiler

def main():

    if len(sys.argv) < 3:
        print("Usage:")
        print("py ufo.py run <file.ufo>")
        return
    
    command = sys.argv[1]

    filename = sys.argv[2]

    compiler = Compiler()

    if command == "run":
        output = compiler.compile(filename)

        print("Compilation successful!\n")

        subprocess.run(["python", str(output)])

    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()