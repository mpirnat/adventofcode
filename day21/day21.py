#!/usr/bin/env python

"""
Solve day 21 of Advent of Code.

http://adventofcode.com/day/21

"""

import copy
import itertools


class Character:

    def __init__(self, name='', hit_points=1,
            natural_damage=0, natural_defense=0,
            weapon=None, armor=None, rings=None):
        self.name = name
        self.hit_points = hit_points
        self.natural_damage = natural_damage
        self.natural_defense = natural_defense
        self.weapon = weapon
        self.armor = armor
        self.rings = rings or []

    @property
    def damage(self):
        return (self.natural_damage +
                (self.weapon.damage if self.weapon else 0) +
                (self.armor.damage if self.armor else 0) +
                sum([x.damage for x in self.rings]))

    @property
    def defense(self):
        return (self.natural_defense +
                (self.weapon.defense if self.weapon else 0) +
                (self.armor.defense if self.armor else 0) +
                sum([x.defense for x in self.rings]))

    @property
    def inventory_cost(self):
        return ((self.weapon.cost if self.weapon else 0) +
                (self.armor.cost if self.armor else 0) +
                sum([x.cost for x in self.rings]))

    @property
    def rings(self):
        return self._rings

    @rings.setter
    def rings(self, rings):
        self._rings = [x for x in rings if x]


class Item:

    def __init__(self, name, cost, damage, defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense


class Combat:

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def do_turn(self):
        self.attack(self.character1, self.character2)
        self.attack(self.character2, self.character1)
        return (
                self.winner(self.character1, self.character2) or
                self.winner(self.character2, self.character1))

    def attack(self, attacker, defender):
        if attacker.hit_points > 0:
            defender.hit_points -= self.calculate_damage(attacker, defender)

    def calculate_damage(self, attacker, defender):
        return max([1, attacker.damage - defender.defense])

    def winner(self, candidate, adversary):
        return (candidate.hit_points > 0 and adversary.hit_points <= 0 and
                candidate) or None

    def do_full_combat(self):
        winner = None
        while not winner:
            winner = self.do_turn()
        return winner


WEAPONS = [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greataxe', 74, 8, 0)]


ARMORS = [
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5)]


RINGS = [
        Item('Damage +1', 25, 1, 0),
        Item('Damage +2', 50, 2, 0),
        Item('Damage +3', 100, 3, 0),
        Item('Defense +1', 20, 0, 1),
        Item('Defense +2', 40, 0, 2),
        Item('Defense +3', 80, 0, 3)]


def find_cheapest_winning_loadout(player, enemy):
    cheapest_loadout = float('inf')

    for player, enemy in generate_scenarios(player, enemy):
        winner = Combat(player, enemy).do_full_combat()
        if winner == player and player.inventory_cost < cheapest_loadout:
            cheapest_loadout = player.inventory_cost

    return cheapest_loadout


def find_costliest_losing_loadout(player, enemy):
    costliest_loadout = 0

    for player, enemy in generate_scenarios(player, enemy):
        winner = Combat(player, enemy).do_full_combat()
        if winner == enemy and player.inventory_cost > costliest_loadout:
            costliest_loadout = player.inventory_cost

    return costliest_loadout


def generate_scenarios(player, enemy):
    for weapon in WEAPONS:
        player.weapon = weapon
        for armor in [None] + ARMORS:
            player.armor = armor
            for rings in [None] + \
                    list(itertools.combinations([None] + RINGS, 2)):
                player.rings = rings or []
                yield copy.copy(player), copy.copy(enemy)


if __name__ == '__main__':
    player = Character(name='player', hit_points=100)
    enemy = Character(name='boss', hit_points=104,
            natural_damage=8, natural_defense=1)

    cheapest_loadout = find_cheapest_winning_loadout(player, enemy)
    print("Part 1:", cheapest_loadout)

    costliest_loadout = find_costliest_losing_loadout(player, enemy)
    print("Part 2:", costliest_loadout)
