#!/usr/bin/env python

import unittest
from day04 import find_integer


class Test(unittest.TestCase):

    cases = (
        ('abcdef', 609043),
        ('pqrstuv', 1048970),
    )

    def test_gets_integer(self):
        for (key, expected) in self.cases:
            result = find_integer(key, zeroes=5)
            self.assertEqual(result, expected,
                "Expected {key} to yield {expected}, but got {result}".\
                        format(**locals()))


if __name__ == '__main__':
    unittest.main()
