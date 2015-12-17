#!/usr/bin/env python

"""
Solve day 15 of Advent of Code.

http://adventofcode.com/day/15

"""

import operator
import re
from collections import namedtuple
from functools import reduce
from itertools import product

Ingredient = namedtuple('Ingredient', [
        'name',
        'capacity',
        'durability',
        'flavor',
        'texture',
        'calories',
    ])


def score_recipe(recipe):
    return reduce(operator.mul, [
        max(0, sum([getattr(x, attr) * amt
            for x, amt in recipe]))
            for attr in Ingredient._fields
            if attr not in ('name', 'calories')])


def find_best_recipe(ingredients, calorie_target=None):
    best_score = 0
    best_recipe = None

    for recipe in make_recipes(ingredients, 100):
        calories = sum([x.calories * amt for x, amt in recipe])
        if calorie_target and calories != calorie_target:
            continue

        score = score_recipe(recipe)
        if score > best_score:
            best_score = score
            best_recipe = recipe

    return best_recipe, best_score


def make_recipes(ingredients, max_amount):
    for amounts in product(range(max_amount + 1), repeat=len(ingredients)):
        if sum(amounts) == max_amount:
            yield list(zip(ingredients, amounts))


# Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
if __name__ == '__main__':
    with open('input.txt') as f:
        ingredients = [Ingredient(
            re.findall('(\w+):', line)[0],
            *map(int, re.findall('-?\d+', line)))
            for line in f]
        recipe, score = find_best_recipe(ingredients)
        print("Part 1:", recipe, score)

        recipe, score = find_best_recipe(ingredients, calorie_target=500)
        print("Part 2:", recipe, score)
