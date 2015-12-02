#!/usr/bin/env python

"""
Solve day 2 of Advent of Code.

http://adventofcode.com/day/2
"""

def paper_area_from_dimensions(dimensions):
    """
    Calculate the area of paper necessary for a package.
    """

    (length, width, height) = [int(x) for x in dimensions.split('x')]

    surface_area = (
            (2 * length * width) +
            (2 * width * height) +
            (2 * height * length))

    slack = min([
            (length * width),
            (length * height),
            (height * width)])

    return surface_area + slack


def ribbon_length_from_dimensions(dimensions):
    """
    Calculate the ribbon length necessary for a package.
    """

    (length, width, height) = [int(x) for x in dimensions.split('x')]

    smallest_perimeter = min([
        2 * (length + width),
        2 * (length + height),
        2 * (height + width)])

    bow_length = length * width * height

    return smallest_perimeter + bow_length


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
