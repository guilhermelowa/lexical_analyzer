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
    if state == States.START:
        if isdigit(char):
            return States.NUM_START
        elif isletter(char):
            return States.IDE_START
    if state == States.NUM_START:
        if isdigit(char):
            return States.NUM_FINAL_1
    elif state == States.NUM_FINAL_1:
        if isdigit(char):
            return States.NUM_FINAL_1
        elif char == '.':
            return States.NUM_DOT
    elif state == States.NUM_DOT:
        if isdigit(char):
            return States.NUM_FINAL_2

    elif state == States.IDE_START:
        if isletter(char):
            return States.IDE_FINAL
    elif state == States.IDE_FINAL:
        if isletter(char) or isdigit(char) or char == '_':
            return States.IDE_FINAL

    return States.INVALID_STATE #TODO Save buffer logic

tokens = []
state = States.START

with open('entrada1.txt') as f:
    for line_num, line in enumerate(f.readline())
        for char in line:
            state, save_buffer = next_state(state, char, buffer)
            if save_buffer:
                save_token(line_num, buffer, previous_state)
            previous_state = state
            
