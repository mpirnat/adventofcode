#!/usr/bin/env python

import unittest

from day17 import find_combinations
from day17 import find_shortest_combination
from day17 import find_combinations_of_length


class TestStoringEggnog(unittest.TestCase):

    containers = [20, 15, 10, 5, 5]
    target = 25

    def test_finds_combinations_that_sum_to_target(self):
        combos = find_combinations(self.containers, self.target)
        self.assertEqual(len(combos), 4)
        for combo in combos:
            self.assertEqual(sum(combo), self.target)

    def test_finds_min_containers_needed(self):
        shortest_combo = find_shortest_combination(self.containers, self.target)
        self.assertEqual(len(shortest_combo), 2)

    def test_finds_combos_of_particular_length(self):
        combos = find_combinations_of_length(self.containers, self.target, 2)
        self.assertEqual(len(combos), 3)


if __name__ == '__main__':
    unittest.main()
