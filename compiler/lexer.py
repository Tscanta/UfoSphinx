# The lexer reads the file line by line.
# It breaks each line into pieces called tokens.

# shlex is like Python's smart split(). It keeps quoted text together.
#
# Example:
# name "Ufo Sphinxman"
#
# becomes
#
# ["name", "Ufo Sphinxman"]
#

import shlex 

class Lexer:
    def tokenize(self, filename):
        tokens = [] # We'll store every line's tokens here.

        with open(filename, "r", encoding="utf-8") as file: # Open the .ufo file.

            for line in file: # Reads one line at a time.

                line = line.strip() # Remove spaces/newlines.

                if line == "": # Ignore empty lines
                    continue

                if line.startswith("//"): #Ignore comments with '//'
                    continue

                # Split the line into tokens.
                # shlex keeps quoted text together.

                line_tokens = shlex.split(line) # Split into tokens.

                tokens.append(line_tokens) # Save them.

            # Return all tokenized lines.
            return tokens