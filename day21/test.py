#!/usr/bin/env python

import unittest


from day21 import Character, Item, Combat


class TestCharacters(unittest.TestCase):

    def setUp(self):
        self.character = Character(name='Bob', hit_points=10,
                natural_damage=5, natural_defense=8)

        weapon = Item('Dagger', 8, 4, 0)
        armor = Item('Leather', 13, 0, 1)
        rings = [Item('Damage +1', 25, 1, 0),
                 Item('Defense +1', 20, 0, 1)]
        self.character2 = Character(name='Bob', hit_points=10,
                natural_damage=5, natural_defense=8,
                weapon=weapon, armor=armor, rings=rings)

    def test_has_name(self):
        self.assertEqual(self.character.name, 'Bob')

    def test_has_hit_points(self):
        self.assertEqual(self.character.hit_points, 10)

    def test_calculates_base_damage(self):
        self.assertEqual(self.character.damage, 5)

    def test_calculates_base_defense(self):
        self.assertEqual(self.character.defense, 8)

    def test_calculates_base_inventory_cost(self):
        self.assertEqual(self.character.inventory_cost, 0)

    def test_calculates_modified_damage(self):
        self.assertEqual(self.character2.damage, 10)

    def test_calculates_modified_defense(self):
        self.assertEqual(self.character2.defense, 10)

    def test_calculates_modifed_inventory_cost(self):
        self.assertEqual(self.character2.inventory_cost, 66)


class TestCombat(unittest.TestCase):

    def setUp(self):
        self.char1 = Character(name='player', hit_points=8,
                natural_damage=5, natural_defense=5)
        self.char2 = Character(name='boss', hit_points=12,
                natural_damage=7, natural_defense=2)
        self.combat = Combat(self.char1, self.char2)

    def test_taking_turns(self):
        winner = self.combat.do_turn()
        self.assertEqual(self.char2.hit_points, 9)
        self.assertEqual(self.char1.hit_points, 6)
        self.assertEqual(winner, None)

        winner = self.combat.do_turn()
        self.assertEqual(self.char2.hit_points, 6)
        self.assertEqual(self.char1.hit_points, 4)
        self.assertEqual(winner, None)

        winner = self.combat.do_turn()
        self.assertEqual(self.char2.hit_points, 3)
        self.assertEqual(self.char1.hit_points, 2)
        self.assertEqual(winner, None)

        winner = self.combat.do_turn()
        self.assertEqual(self.char2.hit_points, 0)
        self.assertEqual(self.char1.hit_points, 2)
        self.assertEqual(winner, self.char1)

    def test_full_combat(self):
        self.char1.hit_points = 8
        self.char2.hit_points = 12
        winner = self.combat.do_full_combat()
        self.assertEqual(winner, self.char1)


if __name__ == '__main__':
    unittestmain()
