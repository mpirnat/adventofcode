#!/usr/bin/env python

import unittest
from day12 import lolsum
from day12 import jsonsum


class TestLolSums(unittest.TestCase):

    cases = (
        ([1, 2, 3], 6),
        ({"a":2,"b":4}, 6),
        ([[[3]]], 3),
        ({"a":{"b":4},"c":-1}, 3),
        ({"a":[-1,1]}, 0),
        ([-1,{"a":1}], 0),
        ([], 0),
        ({}, 0),
    )

    def test_sums_discovered_numbers(self):
        for data, expected in self.cases:
            result = lolsum(str(data))
            self.assertEquals(result, expected,
                    "Expected {data} to sum to "
                    "{expected}, got {result}".format(**locals()))


class TestJsonSums(unittest.TestCase):

    cases = (
        ([1, 2, 3], 6),
        ([1,{"c":"red","b":2},3], 4),
        ({"d":"red","e":[1,2,3,4],"f":5}, 0),
        ([1,"red",5], 6),
    )

    def test_sums_discovered_numbers(self):
        for data, expected in self.cases:
            result = jsonsum(data)
            self.assertEquals(result, expected,
                    "Expected {data} to sum to "
                    "{expected}, got {result}".format(**locals()))



if __name__ == '__main__':
    unittest.main()
