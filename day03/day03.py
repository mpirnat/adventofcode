#!/usr/bin/env python

"""
Solve day 3 of Advent of Code.

http://adventofcode.com/day/3
"""

def houses_from_route(route):
    """
    Record all the houses visited on a route as a list of (x,y) tuples.
    """

    # Everybody gets (0,0) for free
    last_house = (0,0)
    houses = [last_house]

    for move in route:
        if move == '^':
            new_house = (last_house[0], last_house[1] + 1)
        elif move == 'v':
            new_house = (last_house[0], last_house[1] - 1)
        elif move == '>':
            new_house = (last_house[0] + 1, last_house[1])
        elif move == '<':
            new_house = (last_house[0] - 1, last_house[1])
        houses.append(new_house)
        last_house = new_house

    return houses


if __name__ == '__main__':

    with open('input.txt') as f:
        # Part 1 - a single traveler uses all route moves
        route = f.read()
        houses = houses_from_route(route)

        print('Part 1 - Unique houses:', len(set(houses)))

        # Part 2 - two travelers alternate route moves
        route1 = route[::2]
        route2 = route[1::2]
        houses1 = houses_from_route(route1)
        houses2 = houses_from_route(route2)

        print ('Part 2 - Unique houses:', len(set(houses1 + houses2)))
