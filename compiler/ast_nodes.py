# ==========================================================
# AST = Abstract Syntax Tree
#
# Every line in the program becomes an object.
#
# Instead of storing dictionaries, we create classes.
# ==========================================================

class AssignmentNode:

    def __init__(self, variable, value):
        self.variable = variable # Variable name
        self.value = value # Assigned value

    def __repr__(self):
        return f"Assignment({self.variable} = {self.value})"

class PrintNode:

    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Print({self.value})"