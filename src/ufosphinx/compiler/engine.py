# compiler.py
#
# This file represents the entire UFOSPHINX compiler.
#
# Its job is to:
# 1. Read a .ufo file.
# 2. Convert it into tokens (Lexer).
# 3. Convert tokens into an AST (Parser).
# 4. Convert the AST into Python code (Generator).
# 5. Save the generated Python file.

from pathlib import Path # Path helps us work with files and folders safely.

# Import each stage of our compiler.
from .lexer import Lexer 
from .parser import Parser
from .generator import Generator

class Compiler:
    def __init__(self):
 
        self.lexer = Lexer() # Create one lexer object
        self.parser = Parser() # Create one parser object
        self.generator = Generator() # Create one generator object


    def compile(self, source_file):
        source_file = Path(source_file) # Convert the filename into a Path object.
        output_file = Path("output/generated.py") # Choose where the generated Python file will be saved.


        # STEP 1: Read the .ufo file and break it into tokens.
        tokens = self.lexer.tokenize(source_file)
        # Example: [name = "Tshedup"] becomes ["name", "=", "Tshedup"]


        # STEP 2: Convert the tokens into an AST.
        ast = self.parser.parse(tokens)
        # Example:
        #
        # AssignmentNode(
        #     variable="name",
        #     value="Tshedup"
        # )


        # STEP 3: Convert the AST into Python code.
        python_code = self.generator.generate(ast)

        # STEP 4: Save the generated Python code into a file.
        self.generator.write_file(output_file, python_code)
        
        return output_file # Return the generated file path so the CLI can run it.