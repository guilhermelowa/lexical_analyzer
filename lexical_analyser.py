import re
from tokens import *
from states import *

def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None

def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127)

def isdelimiter(x):
    return x in delimiters

def add_char(buffer, char):
    buffer.append(char)

def get_token_type(state):
    if state == States.num_final or state == States.num_after_dot_final:
        return "NRO"
    else if state == States.identifier_final:
        return "IDE"
    else:
        return "ERR"

def save_token(state):
    global tokens
    global buffer
    global line_num

    line_num = str(line_num)
    token_type = get_token_type(state)
    tokens.append(f"{line_num} {token_type} {buffer}")

    buffer = ""

def next_state(state, char):
    global buffer 

    # Initial state
    if state == States.start:
        if isdigit(char):
            return States.num_final
        else if char.isalpha():
            return States.identifier_final
        else if char in delimiters:
            return States.delimiter
        else if char == '>' or char == '<' or char == '=':
            return States.rel
        else if char == '!':
            return States.exclamation
        else if char == '&' or char == '|':
            return States.log_incomplete
        else if char == '+':
            return States.art_plus
        else if char == '-':
            return States.art_minus
        else if char == '*':
            return States.art_complete
        else if char == '/':
            return States.slash

    # Numbers
    else if state == States.num_final:
        if isdigit(char):
            return States.num_final
        else if char == '.':
            return States.num_dot
        else:
            save_token(state)
            return States.start
        
    else if state == States.num_dot:
        if isdigit(char):
            return States.num_after_dot_final
        else:
            save_token(States.invalid_state)
            return States.start

    else if state == States.num_after_dot_final:
        if isdigit(char):
            return States.num_after_dot_final
        else:
            save_token(state, char)
            return States.start

    # Identifiers
    else if state == States.identifier_final:
        if char.isalpha() or isdigit(char) or char == '_':
            return States.identifier_final
        
    # Relational operators
    else if state == States.rel:
        if char == '=':
            return States.rel_equal
    else if state == States.exclamation:
        if char == '=':
            return States.rel_equal

    # Logic operators
    else if state == States.log_incomplete:
        if char == '&' or char == '|':
            return States.log_complete

    # Arithmetic operators
    else if state == States.art_plus:
        if char == '+':
            return States.art_complete
    else if state == States.art_minus:
        if char == '-':
            return States.art_complete

    # Comentaries
    else if state == States.slash:
        if char == '/':
            return States.com_line
        else if char == '*':
            return States.com_block

    else if state == States.com_line:
        if char == '\n':
            return States.com_line_complete
        return States.com_line
    else if state == States.com_block:
        if char == '*':
            return States.com_block_after_asterisk
        return States.com_block
    else if state == States.com_block_after_asterisk:
        if char == '*':
            return States.com_block_after_asterisk
        else if char == '/':
            return States.com_block_complete
        return States.com_block_complete

    return States.invalid_state

tokens = []
state = States.start
buffer = ''

#TODO organize final_states
final_states = [States.num_final, States.num_after_dot_final, States.rel_equal, States.rel, States.exclamation, States.identifier_final, States.log_complete, States.art_complete, States.art_plus, States.art_minus, States.slash, States.delimiter, States.com_block_complete, States.com_line_complete]

with open('input/entrada1.txt') as f:
    for line_num, line in enumerate(f.readline()):
        for char in line:
            state = next_state(state, char)
            if char != ' ':
                buffer += char
