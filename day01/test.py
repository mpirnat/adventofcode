#!/usr/bin/env python

import unittest
from day01 import floor_from_instructions
from day01 import position_of_first_basement


class TestFindFloorFrominstructions(unittest.TestCase):

    """
    Test that we can take in a set of "instructions"
    and get the right value for the "floor" Santa
    ends up on.
    """

    cases = (
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    )

    def test_gets_floor_from_instructions(self):
        for (instructions, expected) in self.cases:
            result = floor_from_instructions(instructions)
            self.assertEqual(result, expected,
                "Expected {instructions} to yield {expected}, but got {result}".\
                        format(**locals()))


class TestFindPositionOfFirstBasement(unittest.TestCase):

    """
    Test that we can find the position of the
    first instruction that causes Santa to
    end up in the "basement"; ie the first
    time we get a -1 result.
    """

    cases = (
        (")", 1),
        ("()())", 5),
    )

    def test_finds_position_of_first_basement(self):
        for (instructions, expected) in self.cases:
            result = position_of_first_basement(instructions)
            self.assertEqual(result, expected,
                "Expected {instructions} to yield {expected}, but got {result}".\
                        format(**locals()))


if __name__ == '__main__':
    unittest.main()
