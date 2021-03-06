from enum import Enum
class States(Enum):
    invalid_state = -1
    start = 0

    num = 2
    num_dot = 3
    num_after_dot = 4

    ide = 6

    rel_greater = 7
    rel_greater_equal = 8
    rel_less = 9
    rel_less_equal = 10
    rel_equal = 11
    rel_comparison = 12
    rel_exclamation = 13
    rel_different = 14