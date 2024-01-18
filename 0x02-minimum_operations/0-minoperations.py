#!/usr/bin/python3
"""0-minoperations.py"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    """
    if n <= 1:
        return 0
    o = 0
    d = 2
    while n > 1:
        while n % d == 0:
            o += d
            n //= d
        d += 1

    return o
