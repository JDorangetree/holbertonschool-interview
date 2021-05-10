#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    'return boolean'
    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False
    for i in range(1, len(boxes)):
        flag = False
        for j in range(len(boxes)):
            flag = i in boxes[j] and i != j
            if flag:
                break
        if flag is False:
            return False
    return True
