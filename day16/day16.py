#!/usr/bin/env python

"""
Solve day 16 of Advent of Code.

http://adventofcode.com/day/16

"""

import re
from functools import reduce


SUE_NUM = re.compile('Sue (\d+):')
SUE_COMPOUNDS = re.compile('(\w+): (\d+)')


if __name__ == '__main__':
    with open('input.txt') as f:
        sues = {SUE_NUM.findall(line)[0]: dict([(x, int(y))
            for x, y in SUE_COMPOUNDS.findall(line)])
            for line in f}

        data = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1,
        }

        suspects = [{x for x in sues.keys()
            if sues[x].get(key) in (data[key], None)}
            for key in data.keys()]
        suspect = list(reduce(set.intersection, suspects))[0]
        print("Part 1:", suspect, sues[suspect])


        suspects = {x for x in sues.keys()
            if (sues[x].get('cats') is None or
                sues[x].get('cats') > data['cats']) and
               (sues[x].get('trees') is None or
                sues[x].get('trees') > data['trees']) and
               (sues[x].get('pomeranians') is None or
                sues[x].get('pomeranians') < data['pomeranians']) and
               (sues[x].get('goldfish') is None or
                sues[x].get('goldfish') < data['goldfish']) and
               (sues[x].get('children') is None or
                sues[x].get('children') == data['children']) and
               (sues[x].get('samoyeds') is None or
                sues[x].get('samoyeds') == data['samoyeds']) and
               (sues[x].get('akitas') is None or
                sues[x].get('akitas') == data['akitas']) and
               (sues[x].get('vizslas') is None or
                sues[x].get('vizslas') == data['akitas']) and
               (sues[x].get('cars') is None or
                sues[x].get('vizslas') == data['vizslas']) and
               (sues[x].get('cars') is None or
                sues[x].get('cars') == data['cars']) and
               (sues[x].get('perfumes') is None or
                sues[x].get('perfumes') == data['perfumes'])}
        print("Part 2:", suspects)



