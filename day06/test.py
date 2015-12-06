#!/usr/bin/env python

import unittest
from day06 import Part1, Part2


class TestPart1(unittest.TestCase):

    cases = (
        ('turn on 0,0 through 1,1', 4),
        ('turn off 0,1 through 1,1', 2),
        ('toggle 0,0 through 1,0', 0),
        ('toggle 0,0 through 1,1', 4),
    )

    def test_maniupulates_lights(self):
        lights = Part1(rows=10, cols=10, default=False)

        for (command, expected) in self.cases:
            lights.do_command(command)
            result = lights.sum_lights()
            self.assertEqual(result, expected,
                "Expected {command} to yield {expected}, but got {result}".\
                        format(**locals()))


class TestPart2(unittest.TestCase):

    cases = (
        ('turn on 0,0 through 1,1', 4),
        ('turn off 0,1 through 1,1', 2),
        ('turn off 0,1 through 5,5', 2), # prove we don't drop below 0
        ('toggle 0,0 through 1,0', 6),
        ('toggle 0,0 through 1,1', 14),
    )

    def test_manipulates_lights(self):
        lights = Part2(rows=10, cols=10, default=0)

        for (command, expected) in self.cases:
            lights.do_command(command)
            result = lights.sum_lights()
            self.assertEqual(result, expected,
                "Expected {command} to yield {expected}, but got {result}".\
                        format(**locals()))



if __name__ == '__main__':
    unittest.main()
