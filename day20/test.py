#!/usr/bin/env python

import unittest

from day20 import next_house


class TestElfDelivery(unittest.TestCase):

    expected = [10, 30, 40, 70, 60, 120, 80, 150, 130]

    def test_gets_expected_presents(self):
        i = 0
        for presents in next_house():
            self.assertEqual(presents, self.expected[i])
            i += 1
            if i == 9:
                break


if __name__ == '__main__':
    unittestamain()
