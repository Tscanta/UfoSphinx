# ==========================================
# UFOSPHINX CLI
#
# This file is what the user runs.
#
# Example:
#
# py ufo.py run examples/hello.ufo
# ==========================================

import sys
import subprocess

from src.ufosphinx.compiler.engine import Compiler

def main():

    # No arguments were given.
    if len(sys.argv) < 2:
        print("ufo <file.ufo>")
        print("ufo run <file.ufo>")
        return
    
    compiler = Compiler() # Creating the compiler
    
    first = sys.argv[1]

    filename = sys.argv[2]

    # ----------------------------
    # Shortcut:
    #
    # ufo hello.ufo
    # ----------------------------
    if first.endswith(".ufo"):
        filename = first
        output = compiler.compile(filename)
        print("Compilation successful!\n")
        subprocess.run(["python", str(output)])
        return

    # ----------------------------
    # Normal command:
    #
    # ufo run hello.ufo
    # ----------------------------
    if first == "run":

        if len(sys.argv) < 3:
            print("Missing filename.")
            return

        filename = sys.argv[2]

        output = compiler.compile(filename)

        print("Compilation successful!\n")

        subprocess.run(["python", str(output)])

        return
    
    print(f"Unknown command: {first}")


if __name__ == "__main__":
    main()