#!/usr/bin/env python

"""
Solve day 14 of Advent of Code.

http://adventofcode.com/day/14

"""

import re


class Reindeer:

    def __init__(self, name, speed, flight_time, rest_time):
        self.name = name
        self.speed = speed
        self.flight_time = flight_time
        self.rest_time = rest_time

        self.distance_traveled = 0
        self.flying = True
        self.time_in_state = 0

        self.points = 0

    def __str__(self):
        return "{0} distance: {1} points: {2}".format(
                self.name, self.distance_traveled, self.points)

    def __repr__(self):
        return str(self)

    def advance(self):
        if self.flying:
            self.distance_traveled += self.speed

        self.time_in_state += 1

        if self.flying and self.time_in_state == self.flight_time:
            self.flying = False
            self.time_in_state = 0
        elif not self.flying and self.time_in_state == self.rest_time:
            self.flying = True
            self.time_in_state = 0


def make_reindeer(data):
    reindeer = []
    for line in data:
        match = re.search(r'^(\w+) can fly (\d+) .* (\d+) .* (\d+) .*$', line)
        name, speed, flight_time, rest_time = match.groups()
        reindeer.append(Reindeer(
                name=name,
                speed=int(speed),
                flight_time=int(flight_time),
                rest_time=int(rest_time)))
    return reindeer


def award_points(reindeer):
    best_distance = max([deer.distance_traveled for deer in reindeer])
    for deer in reindeer:
        if deer.distance_traveled == best_distance:
            deer.points += 1


def run_race(reindeer, seconds):
    for i in range(seconds):
        for deer in reindeer:
            deer.advance()
        award_points(reindeer)


if __name__ == '__main__':
    with open('input.txt') as f:
        reindeer = make_reindeer(f.readlines())
        run_race(reindeer, 2503)
        reindeer.sort(key=lambda deer: deer.distance_traveled)
        print("Part 1:", reindeer[-1].name, reindeer[-1].distance_traveled)

        f.seek(0)
        reindeer = make_reindeer(f.readlines())
        run_race(reindeer, 2503)

        reindeer.sort(key=lambda deer: deer.points)
        print("Part 2:", reindeer[-1].name, reindeer[-1].points)
