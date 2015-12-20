#!/usr/bin/env python

"""
Solve day 20 of Advent of Code.

http://adventofcode.com/day/20

"""

import numpy


def deliver_presents(max_houses):
    houses1 = numpy.zeros(max_houses)
    houses2 = numpy.zeros(max_houses)

    for elf in range(1, max_houses):
        houses1[elf::elf] += 10 * elf
        houses2[elf:(elf+1)*50:elf] += 11 * elf

    return houses1, houses2


def first_house_with_presents(houses, presents):
    return numpy.nonzero(houses >= presents)[0][0]


if __name__ == '__main__':

    max_houses = 10000000
    houses1, houses2 = deliver_presents(max_houses)

    min_presents = 36000000
    part1 = first_house_with_presents(houses1, min_presents)
    part2 = first_house_with_presents(houses2, min_presents)

    print("Part 1:", part1)
    print("Part 2:", part2)
