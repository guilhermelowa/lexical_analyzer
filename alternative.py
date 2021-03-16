import os
import re
from states import *
from tokens import *


def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None

def isletter(x):
     return re.match(r'([A-Za-z])', x) is not None

def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127) and not (ord(x) == 34)

def get_next_state(state, char):
    global line

    # Start
    if state == States.start:
        if char == ' ':
            return States.space
        elif char == "\n":
            return States.new_line
        elif isdigit(char):
            return States.num_final
        elif isletter(char):
            return States.identifier_final
        elif char in delimiters:
            return States.delimiter
        elif char == '>' or char == '<' or char == '=':
            return States.relational_final
        elif char == '!':
            return States.exclamation
        elif char == '&':
            return States.log_and
        elif char == '|':
            return States.log_or
        elif char == '+':
            return States.art_plus
        elif char == '-':
            return States.art_minus
        elif char == '*':
            return States.art_complete
        elif char == '/':
            return States.slash
        elif char == "\"":
            return States.string
        else:
            return States.invalid_symbol

    # Numbers
    elif state == States.num_final:
        if isdigit(char):
            return States.num_final
        elif char == '.':
            return States.num_dot
    elif state == States.num_dot:
        if isdigit(char):
            return States.num_after_dot_final
    elif state == States.num_after_dot_final:
        if isdigit(char):
            return States.num_after_dot_final

    # Identifier
    elif state == States.identifier_final:
        if isletter(char) or isdigit(char) or char == '_':
            return States.identifier_final

    # Relational
    elif state == States.relational_final:
        if char == '=':
            return States.relational_equal_final
    elif state == States.exclamation:
        if char == '=':
            return States.relational_equal_final

    # Logic operators
    elif state == States.log_and:
        if char == '&':
            return States.log_complete
    elif state == States.log_or:
        if char == '|':
            return States.log_complete

    # Arithimetic operators
    elif state == States.art_plus:
        if char == '+':
            return States.art_complete
    elif state == States.art_minus:
        if char == '-':
            return States.art_complete

    # Comentaries
    elif  state == States.slash:
        if char == '/':
            return States.com_line
        elif char == '*':
            return States.com_block

    elif state == States.com_line:
        if char == '\n':
            line += 1
            return States.com_line_complete
        return States.com_line

    elif state == States.com_block:
        if char == '*':
            return States.com_block_after_asterisk
        elif char == '\n':
            line += 1
        return States.com_block
    elif state == States.com_block_after_asterisk:
        if char == '*':
            return States.com_block_after_asterisk
        elif char == '/':
            return States.com_block_complete
        elif char == '\n':
            line += 1
        return States.com_block

    #String 
    elif state == States.string:
        if char == '\\':
            return States.string_escape
        if isletter(char) or char.isdigit() or issymbol(char):
            return States.string
        if char == "\"":
            return States.string_final
        if char == "\n" or char == os.linesep:
            return States.invalid_state
        else:
            return States.string_error
    elif state == States.string_escape:
        if char == "\"":
            return States.string_escape_quote
        elif char == "\\":
            return States.string_escape
        elif isletter(char) or char.isdigit() or issymbol(char):
            return States.string
        else:
            return States.string_error
    elif state == States.string_escape_quote:
        if char == "\"":
            return States.string_final
        elif char == "\\":
            return States.string_escape
        elif isletter(char) or char.isdigit() or issymbol(char):
            return States.string
        else:
            return States.string_error
    elif state == States.string_error:
        if char == "\"" or char == os.linesep or char == "\n":
            return States.string_error_final
        else:
            return States.string_error

    return States.invalid_state 

#TODO Organize dictionary and create default
token_state_dictionary = {
    States.num_final: "NRO",
    States.num_after_dot_final: "NRO",
    States.num_dot: "NMF",
    States.art_complete: "REL",
    States.relational_final: "REL",
    States.relational_equal_final: "REL",
    States.exclamation: "LOG",
    States.log_complete: "LOG",
    States.identifier_final: "IDE",
    States.art_complete: "ART",
    States.art_plus: "ART",
    States.art_minus: "ART",
    States.slash: "ART",
    States.delimiter: "DEL",
    States.string_final: "CAD",
    States.string: "CMF",
    States.string_escape: "CMF",
    States.string_escape_quote: "CMF",
    States.string_error: "CMF",
    States.string_error_final: "CMF",
    States.com_block: "CoMF",
    States.com_block_after_asterisk: "CoMF",
    States.com_line: "CoMF",
    States.log_and: "OpMF",
    States.log_or: "OpMF",
    States.invalid_symbol: "SIB"
}

error_states = [
    "NMF",
    "CMF",
    "CoMF",
    "OpMF",
    "SIB"
]

def next_token(input_string):
    global current_position
    global line
    global tokens
    global errors
    value_buffer = ''
    current_state = States.start
    
    for char in input_string:
        next_state = get_next_state(current_state, char)
        if next_state == States.invalid_state:
            break
        current_state = next_state
        value_buffer += char
    if current_state == States.space:
        current_position += 1
    elif current_state == States.new_line:
        current_position += 1
        line += 1
    else:
        if current_state == States.identifier_final and value_buffer in reserved_words:
            tokens.append(f"{line} PRE {value_buffer}\n")
        elif current_state in token_state_dictionary.keys():
            token_type = token_state_dictionary[current_state]
            tokens.append(f"{line} {token_type} {value_buffer}\n")
            if token_type in error_states:
                errors += 1
        current_position += len(value_buffer)

input_dir = 'tests/'
output_dir = 'tests/'
files_read = 0
files_written = 0

for filename in os.listdir(input_dir):
    if filename.startswith('entrada'):
        file_num = filename.split('.')[0][7:]

        with open(f'{input_dir}{filename}', 'r') as fin:
            file_string = fin.read()
            current_position = 0 #TODO Put these in correct python global variables patterns
            line = 1
            tokens = []
            errors = 0

            while(current_position < len(file_string)):
                next_token(file_string[current_position:])
        if errors == 0:
            print(f"File {filename} read without errors")
        else:
            print(f"Found {errors} errors in {filename}")
        files_read += 1

        with open(f'{output_dir}saida{file_num}.txt', 'w') as fout:
            for token in tokens:
                fout.write(token)
        files_written += 1

print(f"Read {files_read} files\
 \nWrote {files_written} files")
