#!/usr/bin/env python

"""
Solve day 6 of Advent of Code.

http://adventofcode.com/day/6
"""

import re


class Part1:

    def __init__(self, rows=1000, cols=1000, default=None):
        self.grid = self.get_grid(rows, cols, default)

    # This strategy of enumerating a full 1000x1000 2d array is probably a
    # little wasteful, but it's late and it works. #yolo ;-)
    def get_grid(self, rows, cols, default):
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                grid[-1].append(default)
        return grid

    def do_command(self, command):
        action, pos1, pos2 = parse_command(command)

        for i in range(pos1[0], pos2[0]+1):
            for j in range(pos1[1], pos2[1]+1):
                self.grid[i][j] = getattr(self, action)(self.grid[i][j])

    def on(self, cell_value):
        return True

    def off(self, cell_value):
        return False

    def toggle(self, cell_value):
        return not cell_value

    def sum_lights(self):
        return sum(sum(self.grid, []))


class Part2(Part1):

    def on(self, cell_value):
        return cell_value + 1

    def off(self, cell_value):
        return cell_value - 1 if cell_value > 0 else 0

    def toggle(self, cell_value):
        return cell_value + 2


def parse_command(command):
    if 'on' in command:
        action = 'on'
    elif 'off' in command:
        action = 'off'
    elif 'toggle' in command:
        action = 'toggle'

    pos1, pos2 = [x.split(',') for x in
            re.search('\s(\d+,\d+) through (\d+,\d+)', command).groups()]
    pos1 = [int(x) for x in pos1]
    pos2 = [int(x) for x in pos2]

    return action, pos1, pos2


if __name__ == '__main__':

    part1 = Part1(default=False)
    part2 = Part2(default=0)

    with open('input.txt') as f:
        for command in f:
            part1.do_command(command)
            part2.do_command(command)

    print("Part 1:", part1.sum_lights())
    print("Part 2:", part2.sum_lights())
