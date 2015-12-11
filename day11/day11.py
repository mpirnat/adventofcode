#!/usr/bin/env python

"""
Solve day 11 of Advent of Code.

http://adventofcode.com/day/11
"""

import re


BAD_CHARS = re.compile('[ilo]')

chars = 'abcdefghijklmnopqrstuvwxyz'

straights = [chars[i:i+3] for i in range(len(chars)-2)]
INCREASING_STRAIGHT = re.compile('|'.join(straights))

pairs = [char*2 for char in chars]
PAIRS = re.compile('|'.join(pairs))


def make_new_password(password):
    password = next_password(password)
    while not follows_rules(password):
        password = next_password(password)
    return password


def next_password(password):
    pw = [x for x in password]
    pw.reverse()
    for i, char in enumerate(pw):
        try:
            pw[i] = chars[chars.index(char)+1]
        except IndexError:
            pw[i] = chars[0]
        else:
            break
    pw.reverse()
    return ''.join(pw)


def follows_rules(password):
    return not any([
            len(password) != 8,
            not INCREASING_STRAIGHT.search(password),
            BAD_CHARS.search(password),
            len(PAIRS.findall(password)) < 2])


if __name__ == '__main__':
    old_password = "cqjxjnds"
    new_password = make_new_password(old_password)
    print("Part 1:", new_password)

    new_password = make_new_password(new_password)
    print("Part 2:", new_password)
