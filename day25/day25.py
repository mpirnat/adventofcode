#!/usr/bin/env python

"""
Solves day 25 of Advent of Code:

http://adventofcode.com/day/24
"""


def get_next_code(code):
    """
    Generate the next code from the code that precedes it.
    """
    return code * 252533 % 33554393


def get_code_count(row, column):
    """
    Figure out how many times we have to generate codes
    in order to reach the row/column position specified.
    """
    return sum(range(row + column - 1)) + column


def get_code_at_position(row, column, first_code):
    """
    Figure out what the code at a given position is,
    given an initial code at the (1, 1) position.
    """
    code = first_code
    count = get_code_count(row, column)
    for i in range(count - 1):
        code = get_next_code(code)
    return code


if __name__ == '__main__':
    first_code = 20151125
    row = 3010
    column = 3019

    code = get_code_at_position(row, column, first_code)
    print("Part 1:", code)
