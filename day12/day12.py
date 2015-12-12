#!/usr/bin/env python

"""
Solve day 12 of Advent of Code.

http://adventofcode.com/day/12

--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's
where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]),
objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find
all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.
    You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything
red.

Ignore any object (and all of its children) which has any property with the
value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object
    is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire
    structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""

import json
import re


def lolsum(data):
    """
    Probably not reusable for part 2, but haha trololololo...
    """
    return sum([int(x) for x in re.sub(r'[^\d\-,]', '', data).split(',') if x])


def jsonsum(data):
    """
    Oh, all right... Let's walk the json for real. *sigh*
    """
    total = 0
    if isinstance(data, dict):
        vals = data.values()
        if 'red' in vals:
            return 0
        else:
            total += handle_item_sequence(vals)
    elif isinstance(data, list):
        total += handle_item_sequence(data)
    return total


def handle_item_sequence(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, int):
            total += item
        elif isinstance(item, (list, dict)):
            total += jsonsum(item)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
        print("Part 1:", lolsum(data))

        f.seek(0)
        data = json.load(f)
        print("Part 2:", jsonsum(data))
