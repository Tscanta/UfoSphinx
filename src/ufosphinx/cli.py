import sys
import subprocess
from pathlib import Path

from ufosphinx.compiler.engine import Compiler

# Current UFOSPHINX version. (CONST)
VERSION = "UFOSPHINX v0.5.0"

# Print the current version.
def show_version():
    print(VERSION)

# Show all available commands.
def show_help():
    print(f"""
{VERSION}

Usage:

    ufo <file.ufo>
        Compile and run a UFOSPHINX program.

    ufo run <file.ufo>
        Compile and run a UFOSPHINX program.

    ufo build <file.ufo>
        Compile the program without running it.

    ufo version
        Show the current version.

    ufo help
        Show this help menu.

Examples:

    ufo hello.ufo
    ufo run hello.ufo
    ufo build hello.ufo
""")


def run_program(compiler, filename):
    # Make sure the file exists.
    if not Path(filename).exists():
        print(f"UFOSPHINX Error. Returning to spaceship...")
        print(f"File not found: {filename}")
        return

    try:
        # Compile the .ufo file.
        output = compiler.compile(filename)

        print("Compilation successful!\n")

        # Run the generated Python program.
        subprocess.run(["python", str(output)])

    except Exception as error:
        print("UFOSPHINX Compiler Error")
        print(error)


def main():
    # Create the compiler.
    compiler = Compiler()

    # Make sure the user typed something.
    if len(sys.argv) < 2:
        show_help()
        return

    # The first thing after "ufo".
    first = sys.argv[1]

    # Show the version.
    if first == "version":
        show_version()
        return

    # Show the help menu.
    if first == "help":
        show_help()
        return

    # ufo hello.ufo
    if first.endswith(".ufo"):
        run_program(compiler, first)
        return

    # ufo run hello.ufo
    if first == "run":

        if len(sys.argv) < 3:
            print("Missing filename.")
            return

        run_program(compiler, sys.argv[2])
        return

    # ufo build hello.ufo
    if first == "build":

        if len(sys.argv) < 3:
            print("Missing filename.")
            return

        filename = sys.argv[2]

        if not Path(filename).exists():
            print(f"UFOSPHINX Error")
            print(f"File not found: {filename}")
            return

        try:
            compiler.compile(filename)
            print("Build successful!")

        except Exception as error:
            print("UFOSPHINX Compiler Error")
            print(error)

        return

    # The command doesn't exist.
    print(f"Unknown command: {first}")
    print("Type 'ufo help' to see all commands.")


if __name__ == "__main__":
    main()

