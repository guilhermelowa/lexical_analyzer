from enum import Enum
class States(Enum):
    INVALID_STATE = -1
    START = 0
    NUM_START = 1
    NUM_FINAL_1 = 2
    NUM_DOT = 3
    NUM_FINAL_2 = 4
    IDE_START = 5
    IDE_FINAL = 6
