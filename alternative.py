import re

from states import *
from tokens import *


def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None

def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127) and not (ord(x) == 34)


def get_next_state(state, char):
    if state == States.start:
        if char == ' ':
            return States.space
        elif char == "\n":
            return States.new_line
        elif isdigit(char):
            return States.num_final 
        elif char.isalpha():
            return States.identifier_final
        elif char in delimiters:
            return States.delimiter
        elif char == '>' or char == '<' or char == '=':
            return States.relational_final
        elif char == '!':
            return States.exclamation
        elif char == '&' or char == '|':
            return States.log_incomplete
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

    elif state == States.identifier_final:
        if char.isalpha() or isdigit(char) or char == '_':
            return States.identifier_final

    elif state == States.relational_final:
        if char == '=':
            return States.relational_equal_final
    elif state == States.exclamation:
        if char == '=':
            return States.relational_equal_final

    elif state == States.log_incomplete:
        if char == '&' or char == '|':
            return States.log_complete

    elif state == States.art_plus:
        if char == '+':
            return States.art_complete
    elif state == States.art_minus:
        if char == '-':
            return States.art_complete

    elif  state == States.slash:
        if char == '/':
            return States.com_line
        elif char == '*':
            return States.com_block

    elif state == States.com_line:
        if char == '\n':
            return States.com_line_complete
        return States.com_line
    elif state == States.com_block:
        if char == '*':
            return States.com_block_after_asterisk
        return States.com_block
    elif state == States.com_block_after_asterisk:
        if char == '*':
            return States.com_block_after_asterisk
        elif char == '/':
            return States.com_block_complete
        return States.com_block_complete

    #String 
    elif state == States.string:
        if char == '\\':
            return States.string_escape
        if char.isalpha() or char.isdigit() or issymbol(char):
            return States.string
        elif char == "\"":
            return States.string_final
    elif state == States.string_escape:
        if char == "\"":
            return States.string_escape_quote
        elif char == "\\":
            return States.string_escape
        elif char.isalpha() or char.isdigit() or issymbol(char):
            return States.string
    elif state == States.string_escape_quote:
        if char == "\"":
            return States.string_final
        elif char == "\\":
            return States.string_escape
        elif char.isalpha() or char.isdigit() or issymbol(char):
            return States.string

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
    States.com_block: "CoMF",
    States.com_block_after_asterisk: "CoMF",
    States.com_line: "CoMF",
    States.log_incomplete: "OpMF"
}

FILE = open('input/entrada1.txt', 'r')
file_string = FILE.read()
current_position = 0
line = 1
tokens = []

def next_token(input_string):
    global current_position
    global line
    value_buffer = ''
    current_state = States.start
    for char in input_string:
        next_state = get_next_state(current_state, char)
        if next_state == States.invalid_state:
            break
        current_state = next_state
        value_buffer += char
    #TODO Treat comments (just skip position and lines)
    if current_state == States.space:
        current_position += 1
    elif current_state == States.new_line:
        current_position += 1
        line += 1
    else:
        print(f"{token_state_dictionary[current_state]} {value_buffer} {line}")
        current_position += len(value_buffer)


while(current_position < len(file_string)):
    next_token(file_string[current_position:])
