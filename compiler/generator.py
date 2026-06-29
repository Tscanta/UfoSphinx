# The generator takes the AST (Abstract Syntax Tree)
# and converts it into valid Python code.

from .ast_nodes import AssignmentNode, PrintNode

class Generator:
    def generate(self, ast):

        # We'll store every generated Python line here.
        python_code = []

         # Loop through every AST node.
        for node in ast:

            # Variable Assignment
            if isinstance(node, AssignmentNode):

                python_code.append(
                    f"{node.variable} = {repr(node.value)}"
                )

            # Print Statement
            elif isinstance(node, PrintNode):
                python_code.append(
                    f"print({node.value})"
                )
        return python_code
    
    def write_file(self, filename, code):

        with open(filename, "w", encoding="utf-8") as file:

            for line in code:
                file.write(line + "\n")