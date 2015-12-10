#!/usr/bin/env python

import unittest
from day10 import make_sequence


class TestMakingLookAndSaySequences(unittest.TestCase):

    cases = (
        ('1', '11'),
        ('11', '21'),
        ('21', '1211'),
        ('1211', '111221'),
        ('111221', '312211'),
    )

    def test_makes_sequences(self):
        for value, expected in self.cases:
            self.assertEqual(make_sequence(value), expected)


if __name__ == '__main__':
    unittest.main()
