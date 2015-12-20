#!/usr/bin/env python

"""
Solve day 20 of Advent of Code.

http://adventofcode.com/day/20

"""

import itertools


def next_house():
    house = 1
    elf = 1

    while True:
        elves = []
        presents = 0
        for i in range(1, house+1):
            if house % i == 0:
                elves.append(i)
        for elf in elves:
            presents += elf * 10
        #print("house:", house, "elves:", elves, "prs:", presents)
        yield presents
        house += 1



max_divisor_pwr = [13, 5, 4, 4, 3]
prime_divisors = [2, 3, 5, 7, 11]

def orig_number(x):
    t = 1
    for k, j in zip(x, prime_divisors):
        t *= j ** k
    return t


def first_house_with_min_presents(presents, house_limit=None,
        presents_per_elf=10):
    first_house = 1e100
    mi = None

    for i in itertools.product(*[range(i) for i in max_divisor_pwr]):
        elves = 0
        new_house = orig_number(i)

        for j in itertools.product(*[range(k + 1) for k in i]):
            new_elves = orig_number(j)
            if not house_limit or (new_house // new_elves <= house_limit):
                elves += new_elves

        if elves * presents_per_elf >= presents and new_house < first_house:
            first_house = new_house
            mi = i

    return first_house, mi


if __name__ == '__main__':
    presents = 36000000
    print("Part 1:", first_house_with_min_presents(presents))
    print("Part 2:", first_house_with_min_presents(presents, house_limit=50,
        presents_per_elf=11))
