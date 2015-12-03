#!/usr/bin/env python

import unittest
from day03 import houses_from_route


class TestFindHousesVisited(unittest.TestCase):

    cases = (
        ('>', [(0,0), (1,0)]),
        ('^>v<', [(0,0), (0,1), (1,1), (1,0), (0,0)]),
        ('^v^v^v^v^v',
            [(0,0), (0,1),
             (0,0), (0,1),
             (0,0), (0,1),
             (0,0), (0,1),
             (0,0), (0,1),
             (0,0)])
    )

    def test_gets_houses_visited(self):
        for (route, expected) in self.cases:
            result = houses_from_route(route)
            self.assertEqual(result, expected,
                "Expected {route} to yield {expected}, but got {result}".\
                        format(**locals()))


if __name__ == '__main__':
    unittest.main()
