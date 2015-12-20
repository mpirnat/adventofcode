#!/usr/bin/env python

import unittest

from day20 import deliver_presents, find_house_with_min_presents


class TestElfDelivery(unittest.TestCase):

    expected1 = [10, 30, 40, 70, 60, 120, 80, 150, 130]
    expected2 = [11, 33, 44, 77, 66, 132, 88, 165, 143]

    def test_gets_expected_presents(self):
        max_houses = 10
        houses1, houses2 = deliver_presents(max_houses)

        for i, expected in enumerate(self.expected1, 1):
            self.assertEqual(houses1[i], expected)

        for i, expected in enumerate(self.expected2, 1):
            self.assertEqual(houses2[i], expected)

    def test_finds_first_house_with_min_presents(self):
        max_houses = 10
        houses1, houses2 = deliver_presents(max_houses)

        house1 = first_house_with_presents(houses1, 75)
        house2 = first_house_with_presents(houses2, 75)

        self.assertEqual(house1, 6)
        self.assertEqual(house2, 4)


if __name__ == '__main__':
    unittestamain()
