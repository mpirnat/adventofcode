#!/usr/bin/env python

import unittest
from day07 import WiringKit

class TestPart1(unittest.TestCase):

    commands = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]

    expected = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456,
    }

    def test_makes_correct_connections(self):
        kit = WiringKit(self.commands)
        for wire, signal in self.expected.items():
            self.assertEqual(kit.signal_on(wire), signal)


if __name__ == '__main__':
    unittest.main()
