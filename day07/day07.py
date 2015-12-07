#!/usr/bin/env python

"""
Solve day 7 of Advent of Code.

http://adventofcode.com/day/7
"""

class WiringKit:

    def __init__(self, commands):
        self.sources = self.parse_commands(commands)
        self.results = {}

    def parse_commands(self, commands):
        """
        Break down a series of commands to know the sources of all
        possible destination wires. This will let us work backward
        from a given destination to its sources.
        """
        sources = {}
        for command in commands:
            (source, destination) = [x.strip() for x in command.split('->')]
            sources[destination] = source.split()
        return sources

    def signal_on(self, wire):
        """
        Determine the value of the signal on a particular wire.
        """
        try:
            return int(wire)
        except ValueError:
            pass

        if wire not in self.results:
            source = self.sources[wire]

            signal_on = self.signal_on

            if len(source) == 1:
                signal = signal_on(source[0])

            else:
                operator = source[-2]
                if operator == 'AND':
                    signal = signal_on(source[0]) & signal_on(source[-1])
                elif operator == 'OR':
                    signal = signal_on(source[0]) | signal_on(source[-1])
                elif operator == 'LSHIFT':
                    signal = signal_on(source[0]) << signal_on(source[-1])
                elif operator == 'RSHIFT':
                    signal = signal_on(source[0]) >> signal_on(source[-1])
                elif operator == 'NOT':
                    signal = 65535 - signal_on(source[1])

            # Without caching results, the recursion makes the runtime
            # unbearable...
            self.results[wire] = signal

        return self.results[wire]


if __name__ == '__main__':
    with open('input.txt') as f:
        commands = f.readlines()
        kit = WiringKit(commands)
        a = kit.signal_on('a')
        print("Part 1:", a)

        kit.results = {}
        kit.results['b'] = a
        print("Part 2:", kit.signal_on('a'))
