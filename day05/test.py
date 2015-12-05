#!/usr/bin/env python

import unittest
from day05 import is_nice
from day05 import is_new_nice


class TestFindingNiceStrings(unittest.TestCase):

    cases = (
        ('ugknbfddgicrmopn', True),
        ('aaa', True),
        ('jchzalrnumimnmhp', False),
        ('haegwjzuvuyypxyu', False),
        ('dvszwmarrgswjxmb', False),
    )

    def test_identifies_nice_strings(self):
        for (chars, expected) in self.cases:
            result = is_nice(chars)
            self.assertEqual(result, expected,
                "Expected {chars} to yield {expected}, but got {result}".\
                        format(**locals()))


class TestFindingNewNiceStrings(unittest.TestCase):

    cases = (
        ('qjhvhtzxzqqjkmpb', True),
        ('xxyxx', True),
        ('uurcxstgmygtbstg', False),
        ('ieodomkazucvgmuy', False),
    )

    def test_identifies_nice_strings(self):
        for (chars, expected) in self.cases:
            result = is_new_nice(chars)
            self.assertEqual(result, expected,
                "Expected {chars} to yield {expected}, but got {result}".\
                        format(**locals()))

if __name__ == '__main__':
    unittest.main()
