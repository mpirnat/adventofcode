#!/usr/bin/env python

"""
Solve day 9 of Advent of Code.

http://adventofcode.com/day/9
"""

import operator
from collections import defaultdict
from itertools import permutations


class Router:

    def __init__(self, routes):
        self.route_map = self.parse_routes(routes)

    def parse_routes(self, routes):
        route_map = defaultdict(dict)
        for route in routes:
            city1, _, city2, _, distance = route.split()
            route_map[city1][city2] = int(distance)
            route_map[city2][city1] = int(distance)
        return route_map

    def shortest_route(self):
        return self.find_route(operator.lt)

    def longest_route(self):
        return self.find_route(operator.gt)

    def find_route(self, op):
        possible_routes = permutations(self.route_map.keys())
        winner = None
        for route in possible_routes:
            distance = sum(map(lambda x, y:
                    self.route_map[x][y], route[:-1], route[1:]))
            if winner is None or op(distance, winner[1]):
                winner = (route, distance)
        return winner


if __name__ == '__main__':
    with open('input.txt') as f:
        router = Router(f.readlines())
        print("Part 1:", router.shortest_route())
        print("Part 2:", router.longest_route())
