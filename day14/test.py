#!/usr/bin/env python

import unittest

from day14 import make_reindeer, run_race


class TestRacingReindeer(unittest.TestCase):

    data = [
        'Comet can fly 14 km/s for 10 seconds, '
        'but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, '
        'but then must rest for 162 seconds.'
    ]

    def test_makes_reindeer(self):
        reindeer = make_reindeer(self.data)

        self.assertEqual(len(reindeer), 2)

        self.assertEqual(reindeer[0].name, 'Comet')
        self.assertEqual(reindeer[0].speed, 14)
        self.assertEqual(reindeer[0].flight_time, 10)
        self.assertEqual(reindeer[0].rest_time, 127)

        self.assertEqual(reindeer[1].name, 'Dancer')
        self.assertEqual(reindeer[1].speed, 16)
        self.assertEqual(reindeer[1].flight_time, 11)
        self.assertEqual(reindeer[1].rest_time, 162)

    def test_race(self):
        reindeer = make_reindeer(self.data)

        run_race(reindeer, 1)
        Comet, Dancer = reindeer
        self.assertEqual(Comet.distance_traveled, 14)
        self.assertEqual(Dancer.distance_traveled, 16)

        run_race(reindeer, 9)
        self.assertEqual(Comet.distance_traveled, 140)
        self.assertEqual(Dancer.distance_traveled, 160)

        run_race(reindeer, 1)
        self.assertEqual(Comet.distance_traveled, 140)
        self.assertEqual(Dancer.distance_traveled, 176)

        run_race(reindeer, 989)
        self.assertEqual(Comet.distance_traveled, 1120)
        self.assertEqual(Dancer.distance_traveled, 1056)

        self.assertEqual(Comet.points, 312)
        self.assertEqual(Dancer.points, 689)


if __name__ == '__main__':
    unittest.main()
