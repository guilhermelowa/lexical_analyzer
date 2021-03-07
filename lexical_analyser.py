import re
from tokens import *
from states import *

def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None

def isletter(x):
    return re.match(r'([a-z] || [A-Z])', x) is not None

def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127)

def isdelimiter(x):
    return x is in delimiters

def identify_token(previous_state):
    if previous_state in final_states:
        # get which token recognizer it is
    else:  # else invalid
        return "ERR"

def save_token(line_num, buffer, previous_state):
    global tokens

    token_type = identify_token(previous_state)
    tokens.append([line_num, buffer, token_type])  # append output

#TODO Move next state
def next_state(state, char):
    if state == States.start:
        if isdigit(char):
            return States.num 
        elif char.isalpha():
            return States.ide
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


    elif state == States.num:
        if isdigit(char):
            return States.num
        elif char == '.':
            return States.num_dot
    elif state == States.num_dot:
        if isdigit(char):
            return States.num_after_dot
    elif state == States.num_after_dot:
        if isdigit(char):
            return States.num_after_dot

    elif state == States.ide:
        if isletter(char) or isdigit(char) or char == '_':
            return States.ide

    elif state == States.rel:
        if char == '=':
            return States.rel_equal
    elif state == States.exclamation:
        if char == '=':
            return States.rel_equal
        return States.log_complete

    elif state == States.log_incomplete:
        if char == '&' or char == '|':
            return States.log_complete

    elif state == States.art_plus:
        if char == '+':
            return States.art_complete
    elif state == States.art_minus:
        if char == '-':
            return States.art_complete

tokens = []
state = States.START

with open('entrada1.txt') as f:
    for line_num, line in enumerate(f.readline())
        for char in line:
            state, save_buffer = next_state(state, char)
            if save_buffer:
                save_token(line_num, buffer, previous_state)
            previous_state = state
