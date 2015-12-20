#!/usr/bin/env python

"""
Solve day 17 of Advent of Code.

http://adventofcode.com/day/17

"""


def find_combinations(numbers, target, partial=[]):
    """
    Find combinations of numbers that sum to a particular target value;
    return them as a list of lists.
    """
    combos = []

    s = sum(partial)

    if s == target:
        combos.append(partial)

    if s >= target:
        return combos

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        combos.extend(find_combinations(remaining, target, partial + [n]))

    return combos


def find_shortest_combination(numbers, target):
    combos = find_combinations(numbers, target)
    shortest_length = float('inf')
    shortest_combo = None

    for combo in combos:
        combo_length = len(combo)
        if combo_length < shortest_length:
            shortest_length = combo_length
            shortest_combo = combo

    return shortest_combo


def find_combinations_of_length(numbers, target, length):
    all_combos = find_combinations(numbers, target)
    combos = []

    for combo in all_combos:
        if len(combo) == length:
            combos.append(combo)

    return combos


if __name__ == '__main__':
    with open('input.txt') as f:
        target = 150
        containers = [int(x.strip()) for x in f]

        combos = find_combinations(containers, target)
        print("Part 1:", len(combos))

        shortest_combo = find_shortest_combination(containers, target)
        min_combos = find_combinations_of_length(containers, target,
                len(shortest_combo))
        print("Part 2:", len(min_combos))
