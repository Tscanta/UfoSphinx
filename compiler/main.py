from pathlib import Path
from lexer import Lexer
from parser import Parser

def main():
    project_root = Path(__file__).parent.parent # Get the project's root folder
    
    source_file = project_root / "examples" / "hello.ufo" # Build the path safely

    lexer = Lexer() # Create an instance (object) of the Lexer class.
    
    parser= Parser() # Create an instance (object) of the Parser class.
    
    tokens = lexer.tokenize(source_file) # Read and tokenize the .ufo file.

    ast = parser.parse(tokens)

    for node in ast:
        print(node)

if __name__ == "__main__":
    main()
