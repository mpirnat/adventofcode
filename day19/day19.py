#!/usr/bin/env python

"""
Solve day 19 of Advent of Code.

http://adventofcode.com/day/19

"""

import re
from collections import defaultdict


REPLACEMENT = re.compile(r'^(\w+) => (\w+)$')


def parse_input(data):
    replacements = defaultdict(list)
    initial_molecule = ''

    for line in data.splitlines():
        for atom, replacement in REPLACEMENT.findall(line):
            replacements[atom].append(replacement)

        if line and '=>' not in line:
            initial_molecule = line

    return initial_molecule, replacements


def generate_molecules(molecule, replacements):
    new_molecules = []
    for atom, replacements in replacements.items():
        for replacement in replacements:
            start = 0
            i = molecule.find(atom, start)

            while i > -1:
                new_molecules.append(
                        molecule[:i] +
                        replacement +
                        molecule[i+len(atom):])
                start = i + len(atom)
                i = molecule.find(atom, start)

    return set(new_molecules)


def steps_to_make(molecule, replacements):
    steps = 0
    replacements = list(invert_replacements(replacements).items())
    orig_replacements = replacements.copy()

    while molecule != 'e':
        try:
            replacement, atom = max(replacements, key=lambda x: len(x[0]))
        except ValueError:
            replacements = orig_replacements.copy()
            replacement, atom = max(replacements, key=lambda x: len(x[0]))

        i = molecule.rfind(replacement)
        new_molecule = molecule[:i] + molecule[i:].replace(replacement, atom, 1)
        if new_molecule != molecule:
            steps += 1
            replacements = orig_replacements.copy()
            #print(molecule, '=>', new_molecule)
        else:
            replacements.remove((replacement, atom))
        molecule = new_molecule
    return steps


def invert_replacements(replacements):
    new_replacements = {}
    for atom, molecules in replacements.items():
        for molecule in molecules:
            new_replacements[molecule] = atom
    return new_replacements


if __name__ == '__main__':
    with open('input.txt') as f:
        initial_molecule, replacements = parse_input(f.read())
        molecules = generate_molecules(initial_molecule, replacements)
        print("Part 1:", len(molecules))

        print("Part 2:", steps_to_make(initial_molecule, replacements))
