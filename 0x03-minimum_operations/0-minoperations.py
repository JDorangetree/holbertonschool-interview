#!/usr/bin/python3
"""method that calculates the fewest number of operations"""


def minOperations(n):
    """return int"""
    if n < 2:
        return 0
    mul_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                mul_list.append(i)
    return sum(mul_list)
