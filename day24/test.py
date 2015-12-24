#!/usr/bin/env python

import unittest

from day24 import lowest_quantum_entanglement

class TestFindingLowestQuantumEntanglement(unittest.TestCase):

    def test_with_3_groups(self):
        packages = list(range(1,6)) + list(range(7,12))
        qe = lowest_quantum_entanglement(packages, 3)
        self.assertEqual(qe, 99)

    def test_with_4_groups(self):
        packages = list(range(1,6)) + list(range(7,12))
        qe = lowest_quantum_entanglement(packages, 4)
        self.assertEqual(qe, 44)


if __name__ == '__main__':
    unittest.main()
