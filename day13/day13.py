#!/usr/bin/env python

"""
Solve day 12 of Advent of Code.

http://adventofcode.com/day/12

"""

import re
from collections import defaultdict
from itertools import permutations


def parse_input(data):
    guests = defaultdict(dict)
    for line in data:
        match = re.search(
                r'^(\w+) would (\w+) (\d+) .+ (\w+)\.$', line)
        person1, action, happiness, person2 = match.groups()
        happiness = int(happiness)
        if action == 'lose':
            happiness = -happiness
        guests[person1][person2] = happiness
    return guests


def find_best_arrangement(guests):
    best_arrangement = []
    max_happiness = 0

    for arrangement in permutations(guests.keys()):
        feelings = []
        for i, guest in enumerate(arrangement):
            prev_guest = arrangement[i-1]
            try:
                next_guest = arrangement[i+1]
            except IndexError:
                next_guest = arrangement[0]

            feelings.append(guests[guest].get(prev_guest, 0))
            feelings.append(guests[guest].get(next_guest, 0))

        happiness = sum(feelings)
        if happiness > max_happiness:
            best_arrangement = arrangement
            max_happiness = happiness

    return best_arrangement, max_happiness


if __name__ == '__main__':
    with open('input.txt') as f:
        guests = parse_input(f.readlines())
        arrangement, happiness = find_best_arrangement(guests)
        print("Part 1:", arrangement, happiness)

        guests['Me'] = {}
        arrangement, happiness = find_best_arrangement(guests)
        print("Part 2:", arrangement, happiness)
