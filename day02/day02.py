#!/usr/bin/env python

"""
Solve day 2 of Advent of Code.

http://adventofcode.com/day/2
"""

def paper_area_from_dimensions(dimensions):
    """
    Calculate the area of paper necessary for a package.
    """

    dimensions = sorted([int(x) for x in dimensions.split('x')])

    surface_area = 2 * (
            dimensions[0] * dimensions[1] +
            dimensions[0] * dimensions[2] +
            dimensions[1] * dimensions[2])

    slack = dimensions[0] * dimensions[1]

    return surface_area + slack


def ribbon_length_from_dimensions(dimensions):
    """
    Calculate the ribbon length necessary for a package.
    """
    dimensions = sorted([int(x) for x in dimensions.split('x')])

    perimeter = 2 * (dimensions[0] + dimensions[1])
    bow_length = dimensions[0] * dimensions[1] * dimensions[2]

    return perimeter + bow_length


if __name__ == '__main__':
    total_paper = 0
    total_ribbon = 0

    with open('input.txt') as f:
        for dimensions in f:
            dimensions = dimensions.strip()
            total_paper += paper_area_from_dimensions(dimensions)
            total_ribbon += ribbon_length_from_dimensions(dimensions)

    print("Total paper:", total_paper)
    print("Total ribbon:", total_ribbon)
