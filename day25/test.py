#!/usr/bin/env python

import unittest

from day25 import get_next_code, get_code_count, get_code_at_position


class TestGeneratingCodes(unittest.TestCase):

    expected_codes = [
            31916031, 18749137, 16080970, 21629792, 17289845,
            24592653, 8057251, 16929656, 30943339]

    first_code = 20151125

    def test_generates_codes(self):
        code = self.first_code
        for expected in self.expected_codes:
            next_code = get_next_code(code)
            self.assertEqual(next_code, expected)
            code = next_code

    def test_gets_count_of_codes_needed_for_position(self):
        self.assertEqual(get_code_count(1, 1), 1)
        self.assertEqual(get_code_count(2, 1), 2)
        self.assertEqual(get_code_count(1, 2), 3)
        self.assertEqual(get_code_count(2, 2), 5)

    def test_gets_code_at_position(self):
        cases = [
                (1, 1, self.first_code),
                (1, 2, 18749137),
                (5, 5, 9250759),
                (6, 6, 27995004)
            ]

        for row, column, expected in cases:
            self.assertEqual(get_code_at_position(row, column, self.first_code),
                    expected)


if __name__ == '__main__':
    unittest.main()
