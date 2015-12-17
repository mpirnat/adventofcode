#!/usr/bin/env python

import unittest

from day15 import Ingredient, score_recipe, make_recipes, find_best_recipe


class TestScoringRecipes(unittest.TestCase):
    ing1 = Ingredient(
            name='butterscotch',
            capacity=-1,
            durability=-2,
            flavor=6,
            texture=3,
            calories=8)

    ing2 = Ingredient(
            name='cinnamon',
            capacity=2,
            durability=3,
            flavor=-2,
            texture=-1,
            calories=3)

    def test_produces_score(self):
        recipe = [(self.ing1, 44), (self.ing2, 56)]
        score = score_recipe(recipe)
        self.assertEqual(score, 62842880)

    def test_makes_recipes(self):
        ingredients = [self.ing1, self.ing2]
        recipes = list(make_recipes(ingredients, 100))
        self.assertEqual(len(recipes), 101)
        self.assertEqual(list(recipes[0]), [(self.ing1, 0), (self.ing2, 100)])
        self.assertEqual(list(recipes[1]), [(self.ing1, 1), (self.ing2, 99)])
        self.assertEqual(list(recipes[-1]), [(self.ing1, 100), (self.ing2, 0)])

    def test_finds_best_recipe(self):
        ingredients = [self.ing1, self.ing2]
        recipe, score = find_best_recipe(ingredients)
        self.assertEqual(score, 62842880)

    def test_finds_best_calorie_limited_recipe(self):
        ingredients = [self.ing1, self.ing2]
        recipe, score = find_best_recipe(ingredients, calorie_target=500)
        self.assertEqual(score, 57600000)


if __name__ == '__main__':
    unittest.main()
