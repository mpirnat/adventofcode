#!/usr/bin/env python

"""
Solve day 4 of Advent of Code.

http://adventofcode.com/day/4
"""

import hashlib

def find_integer(key, hash_start='0'*5):
    """
    Find the smallest integer such that the md5 hash of the
    given secret key plus the integer yields a hash that
    begins with a certain number of zeroes (default 5).
    """
    hashed = ''
    i = 0
    while not hashed.startswith(hash_start):
        i += 1
        to_hash = (key + str(i)).encode('ascii')
        hashed = hashlib.md5(to_hash).hexdigest()
    return i


if __name__ == '__main__':
    key = 'yzbqklnj'
    print('Part 1:', find_integer(key))
    print('Part 2:', find_integer(key, hash_start='0'*6))
