#!/usr/bin/env python

"""
Solve day 1 of Advent of Code.

http://adventofcode.com/day/1
"""

# Do we go up or down based on the instruction character?
instruction_map= { '(': 1, ')': -1 }

def floor_from_instructions(instructions):
    """
    Get the floor number resulting from a set of instructions.
    """
    return sum([instruction_map.get(x, 0) for x in instructions])


def position_of_first_basement(instructions):
    """
    Find the position in the instructions (1-based) where we
    first visit the "basement" (get a -1 floor number).

    Return -1 if there is no such instruction position.
    """
    for i in range(len(instructions) + 1):
        if floor_from_instructions(instructions[:i]) == -1:
            return i
    return -1


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = f.read()
        print("Part 1:", floor_from_instructions(instructions))
        print("Part 2:", position_of_first_basement(instructions))
