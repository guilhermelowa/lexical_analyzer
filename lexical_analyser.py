import re
from tokens import *


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

tokens = []
state = 0  # TODO: create enum

with open('entrada1.txt') as f:
    for line_num, line in enumerate(f.readline())
        for char in line:
            state, save_buffer = next_state(state, char, buffer)
            if save_buffer:
                save_token(line_num, buffer, previous_state)
            previous_state = state
            
