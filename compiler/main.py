import subprocess
from pathlib import Path
from lexer import Lexer
from parser import Parser
from generator import Generator


def main():

    # Find the project folder.
    project_root = Path(__file__).parent.parent

    # Path to the UFOSPHINX source file.
    source_file = project_root / "examples" / "hello.ufo"

    # Path where generated Python will be saved.
    output_file = project_root / "output" / "generated.py"

    # Create compiler stages.
    lexer = Lexer()
    parser = Parser()
    generator = Generator()

    # Stage 1: Convert text into tokens.
    tokens = lexer.tokenize(source_file)

    # Stage 2: Convert tokens into AST.
    ast = parser.parse(tokens)

    # Stage 3: Convert AST into Python code.
    python_code = generator.generate(ast)

    # Stage 4: Save the generated Python.
    generator.write_file(output_file, python_code)

    print("Running program...\n")
    subprocess.run(["python", output_file])

    print("Compilation successful!")

    print(f"Generated: {output_file}")


if __name__ == "__main__":
    main()