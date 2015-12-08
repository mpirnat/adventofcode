#!/usr/bin/env python

import unittest
from day08 import get_lengths, encode


class TestCheckingLengths(unittest.TestCase):

    def test_gets_correct_counts(self):
        cases = (
            # string,
            # length of code literal,
            # length of string,
            # length of encoded literal
            (r'""', 2, 0, 6),
            (r'"abc"', 5, 3, 9),
            (r'"aaa\"aaa"', 10, 7, 16),
            (r'"\x27"', 6, 1, 11)
        )

        for string, len_literal, len_string, len_encoded in cases:
            lengths = get_lengths(string)
            self.assertEqual(lengths[0], len_literal, string)
            self.assertEqual(lengths[1], len_string, string)
            self.assertEqual(lengths[2], len_encoded, string)

    def test_encodes_string_literal(self):
        cases = (
            (r'""', r'"\"\""'),
            (r'"abc"', r'"\"abc\""'),
            (r'"aaa\"aaa"', r'"\"aaa\\\"aaa\""'),
            (r'"\x27"', r'"\"\\x27\""')
        )
        for string, expected in cases:
            self.assertEqual(encode(string), expected)

if __name__ == '__main__':
    unittest.main()
