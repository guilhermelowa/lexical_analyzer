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
def next_state(state, char, buffer):
    if state == States.start:
        if isdigit(char):
            return States.num 
        elif isletter(char):
            return States.ide
        elif char == '>' or char == '<' or char == '=':
            return States.rel
        elif char == '!':
            return States.exclamation

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

    return States.invalid_state #TODO Save buffer logic

tokens = []
state = States.START

with open('entrada1.txt') as f:
    for line_num, line in enumerate(f.readline())
        for char in line:
            state, save_buffer = next_state(state, char, buffer)
            if save_buffer:
                save_token(line_num, buffer, previous_state)
            previous_state = state
