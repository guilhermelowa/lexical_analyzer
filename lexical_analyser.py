import re
from tokens import *
from states import *

def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None

def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127)

def isdelimiter(x):
    return x in delimiters

# def identify_token(previous_state):
#     if previous_state in final_states:
#         # get which token recognizer it is
#     else:  # else invalid
#         return "ERR"

# def save_token(line_num, buffer, previous_state):
#     global tokens

#     token_type = identify_token(previous_state)
#     tokens.append([line_num, buffer, token_type])  # append output

#TODO Move next state
def next_state(state, char):
    if state == States.start:
        if isdigit(char):
            return States.num_final 
        elif char.isalpha():
            return States.identifier_final
        elif char in delimiters:
            return States.delimiter
        elif char == '>' or char == '<' or char == '=':
            return States.rel
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

    elif state == States.rel:
        if char == '=':
            return States.rel_equal
    elif state == States.exclamation:
        if char == '=':
            return States.rel_equal

    elif state == States.log_incomplete:
        if char == '&' or char == '|':
            return States.log_complete

    elif state == States.art_plus:
        if char == '+':
            return States.art_complete
    elif state == States.art_minus:
        if char == '-':
            return States.art_complete

    elif state == States.slash:
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

    return States.invalid_state

tokens = []
previous_state = States.start
buffer = ''

#TODO organize final_states
final_states = [States.num_final, States.num_after_dot_final, States.rel_equal, States.rel, States.exclamation, States.identifier_final, States.log_complete, States.art_complete, States.art_plus, States.art_minus, States.slash, States.delimiter, States.com_block_complete, States.com_line_complete]

with open('input/entrada1.txt') as f:
    for line_num, line in enumerate(f.readline()):
        for char in line:
            state = next_state(previous_state, char)
            #if condition:
                #TODO Save token logic
            previous_state = state
            buffer += char
