#!/usr/bin/env python

import unittest

from day19 import generate_molecules, parse_input, steps_to_make


class TestCalibratingUnit(unittest.TestCase):

    replacements = {
        'H': ['HO', 'OH'],
        'O': ['HH'],
    }

    initial_molecule = 'HOH'

    input_data = \
"""H => HO
H => OH
O => HH

HOH"""

    def test_generates_possible_molecules(self):
        molecules = generate_molecules(self.initial_molecule, self.replacements)
        self.assertEqual(molecules, {'HOOH', 'HOHO', 'OHOH', 'HHHH'})

    def test_ignores_surrounding_characters(self):
        molecules = generate_molecules('H2O', {'H': ['OO']})
        self.assertEqual(molecules, {'OO2O'})

    def test_parses_input_data(self):
        initial_molecule, replacements = parse_input(self.input_data)
        self.assertEqual(replacements, self.replacements)
        self.assertEqual(initial_molecule, self.initial_molecule)


class TestGeneratingMolecule(unittest.TestCase):

    replacements = {
        'e': ['H', 'O'],
        'H': ['HO', 'OH'],
        'O': ['HH'],
    }

    def test_finds_steps_to_make_molecule(self):
        target = 'HOH'
        steps = steps_to_make(target, self.replacements)
        self.assertEqual(steps, 3)

        target = 'HOHOHO'
        steps = steps_to_make(target, self.replacements)
        self.assertEqual(steps, 6)





if __name__ == '__main__':
    unittestamain()
