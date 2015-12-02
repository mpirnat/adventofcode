#!/usr/bin/env python

import unittest
from day02 import paper_area_from_dimensions
from day02 import ribbon_length_from_dimensions


class TestFindWrappingPaperSquareFootage(unittest.TestCase):

    cases = (
        ('2x3x4', 58),
        ('1x1x10', 43),
    )

    def test_gets_square_footage(self):
        for (dimensions, expected) in self.cases:
            result = paper_area_from_dimensions(dimensions)
            self.assertEqual(result, expected,
                "Expected {dimensions} to yield {expected}, but got {result}".\
                        format(**locals()))


class FindRibbonLength(unittest.TestCase):

    cases = (
        ('2x3x4', 34),
        ('1x1x10', 14),
    )

    def test_gets_ribbon_length(self):
        for (dimensions, expected) in self.cases:
            result = ribbon_length_from_dimensions(dimensions)
            self.assertEqual(result, expected,
                "Expected {dimensions} to yield {expected}, but got {result}".\
                        format(**locals()))



if __name__ == '__main__':
    unittest.main()
