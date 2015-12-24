#!/usr/bin/env python

"""
Solves day 24 of Advent of Code

http://adventofcode.com/day/24

Props to the leaderboard folks on Reddit who made me realize
I was way, way overengineering the problem.
"""

import operator
from functools import reduce
from itertools import combinations


def lowest_quantum_entanglement(packages, num_groups):
    """
    Find the minimum quantum entanglement for the minimum-sized
    group of packages split into num_groups groups of equal weight.
    """
    target_weight = sum(packages) // num_groups
    max_combo_length = len(packages) // num_groups
    best_combo_length = float('inf')
    best_qe = float('inf')

    #print(packages, num_groups, target_weight, max_combo_length)

    # Limit our search space to combinations no larger than the number
    # of packages divided by the number of groups; no "minimum length"
    # combination will ever be more than 1/n of the packages.
    for i in range(1, max_combo_length + 1):

        # Build combinations of increasing size...
        for combo in combinations(packages, i):

            # Throw out anything that won't give us a balanced load
            if sum(combo) != target_weight:
                continue

            # We only want the minimum length combos (to maximize
            # Santa's legroom)
            combo_length = len(combo)
            if combo_length > best_combo_length:
                continue
            best_combo_length = combo_length

            # Calculate the "quantum entanglement" and see how it fares
            qe = reduce(operator.mul, combo)
            #print(combo, sum(combo), qe)
            best_qe = min(best_qe, qe)

    return best_qe


if __name__ == '__main__':
    with open('input.txt') as f:
        packages = [int(x) for x in f.readlines()]

        print("Part 1:", lowest_quantum_entanglement(packages, 3))
        print("Part 2:", lowest_quantum_entanglement(packages, 4))
