# The parser understands commands.

from ast_nodes import AssignmentNode, PrintNode

class Parser:

    def parse(self, tokens): # Receiving the output from Lexer

        ast = []

        for line in tokens:

            if not line: # Ignore empty lines
                continue

            # PRINT
            if line[0] in ["print", "say", "display"]:
                node = PrintNode(line[1])
                ast.append(node)
                continue

            # ASSIGNMENT
            variable = line[0]

            if "=" in line: # name = "Sphinx"
                value = line[-1]
            else: # name "Sphinx"
                value = line[1]

            value = self.parse_value(value)
            node = AssignmentNode(variable, value)

            ast.append(node)

        return ast
    
    # Type Casting
    def parse_value(self, value):

        # Boolean
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False

        # Integer
        try:
            return int(value)
        except ValueError:
            pass

        # Float
        try:
            return float(value)
        except ValueError:
            pass

        # Otherwise it's a string
        return value
