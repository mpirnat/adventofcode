#!/usr/bin/env python

import unittest
from day09 import Router


class TestFindingShortestRoute(unittest.TestCase):

    routes = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]

    def test_finds_shortest_route(self):
        router = Router(self.routes)
        self.assertEqual(router.shortest_route()[1], 605)

    def test_finds_longest_route(self):
        router = Router(self.routes)
        self.assertEqual(router.longest_route()[1], 982)


if __name__ == '__main__':
    unittest.main()
