#!/usr/bin/env python

"""
Solve day 10 of Advent of Code.

http://adventofcode.com/day/10
"""


def make_sequence(value):
    cur_char = None
    cur_count = 0
    sequence = []

    for char in value:

        # Look for change to new character;
        # emit the next part of the sequence
        # and reset the count.
        if cur_char != char and cur_char is not None:
            sequence.extend([str(cur_count), cur_char])
            cur_count = 0

        # Record the current character and
        # increment its count.
        cur_char = char
        cur_count += 1

    # End of the string is its own 'transition';
    # emit the next part of the sequence
    sequence.extend([str(cur_count), cur_char])

    return ''.join(sequence)


if __name__ == '__main__':
    sequence = '1113222113'

    for i in range(40):
        sequence = make_sequence(sequence)
    print("Part 1:", len(sequence))

    for i in range(10):
        sequence = make_sequence(sequence)
    print("Part 2:", len(sequence))
