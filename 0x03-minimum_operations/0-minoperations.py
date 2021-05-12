#!/usr/bin/python3
"""method that calculates the fewest number of operations"""


def minOperations(n):
    """return an integer"""
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
        


def multiples(n):
    multiples = []
    for i in range(1, n +1):
        module = n%i
        if module == 0 and i != n:
            multiples.append(i)
    return(sorted(multiples)[-2:])
