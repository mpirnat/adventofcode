#!/usr/bin/env python

"""
Solve day 5 of Advent of Code.

http://adventofcode.com/day/5
"""

import re


def is_nice(chars):
    """
    Rules for part 1
    """
    return (
            has_three_vowels(chars) and
            has_2x_in_row(chars) and
            does_not_have_bad_pairs(chars)
    )


def has_three_vowels(chars):
    """
    It contains at least three vowels (aeiou only), like aei, xazegov, or
    aeiouaeiouaeiou.
    """
    vowels = 'aeiou'
    if sum([chars.count(x) for x in vowels]) >= 3:
        return True
    return False


def has_2x_in_row(chars):
    """
    It contains at least one letter that appears twice in a row, like xx,
    abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    """
    if re.search(r'(\w)\1+', chars):
        return True
    return False


def does_not_have_bad_pairs(chars):
    """
    It does not contain the strings ab, cd, pq, or xy, even if they are part of
    one of the other requirements.
    """
    bad_pairs = ['ab', 'cd', 'pq', 'xy']
    if any([x in chars for x in bad_pairs]):
        return False
    return True


def is_new_nice(chars):
    """
    New rules for part 2
    """
    return (
        has_non_overlapping_pairs(chars) and
        has_repeat_char_with_one_between(chars)
    )


def has_non_overlapping_pairs(chars):
    """
    It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    aaa (aa, but it overlaps).
    """
    if re.search(r'(\w\w).*\1', chars):
        return True
    return False


def has_repeat_char_with_one_between(chars):
    """
    It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    if re.search(r'(\w)[^\1]\1', chars):
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        words = f.readlines()
        print("Part 1:", sum([is_nice(x) for x in words]))
        print("Part 2:", sum([is_new_nice(x) for x in words]))

