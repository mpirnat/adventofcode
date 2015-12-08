#!/usr/bin/env python

"""
Solve day 8 of Advent of Code.

http://adventofcode.com/day/8
"""

# because security
import ast


def get_lengths(string):
    return (
        len(string),
        len(ast.literal_eval(string)),
        len(encode(string)),
    )


def encode(string):
    return '"%s"' % string.replace('\\', '\\\\').replace('"', '\\"')


if __name__ == '__main__':
    len_strings = 0
    len_literals = 0
    len_encodeds = 0

    with open('input.txt') as f:
        for string in f:
            len_literal, len_string, len_encoded = get_lengths(string.strip())
            len_literals += len_literal
            len_strings += len_string
            len_encodeds += len_encoded

    print("Part 1:", len_literals - len_strings)
    print("Part 2:", len_encodeds - len_literals)


