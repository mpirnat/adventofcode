#!/usr/bin/env python

import unittest

from day13 import parse_input, find_best_arrangement


class TestFindingBestArrangement(unittest.TestCase):

    data = [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.',
    ]

    def test_makes_guest_dict(self):
        guests = parse_input(self.data)
        self.assertEquals(guests['Alice']['Bob'], 54)
        self.assertEquals(guests['Alice']['Carol'], -79)
        self.assertEquals(guests['David']['Alice'], 46)

    def test_finds_best_arrangement(self):
        guests = parse_input(self.data)
        arrangement, happiness = find_best_arrangement(guests)
        self.assertEquals(len(arrangement), 4)
        self.assertEquals(happiness, 330)

    def test_finds_best_arrangement_with_noncommittal_guest(self):
        guests = parse_input(self.data)
        guests['Me'] = {}
        arrangement, happiness = find_best_arrangement(guests)
        self.assertEquals(len(arrangement), 5)
        self.assertEquals(happiness, 286)




if __name__ == '__main__':
    unittest.main()
