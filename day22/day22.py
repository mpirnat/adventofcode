#!/usr/bin/env python

"""
Solve day 22 of Advent of Code.

http://adventofcode.com/day/22

Right now this implementation is somewhat flaky and doesn't reliably
find the right winning scenarios but it did produce the right output
a couple of times. It should probably be rewritten if I can muster
up the energy to care.
"""

import copy
import random


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


class MagicUser(Character):

    def __init__(self, name='', hit_points=1, mana=0,
            natural_damage=0, natural_defense=0,
            weapon=None, armor=None, rings=None):
        super(MagicUser, self).__init__(name=name, hit_points=hit_points)
        self.mana = mana
        self.mana_spent = 0
        self.temporary_defense = 0

    @property
    def defense(self):
        return (self.natural_defense + self.temporary_defense)


class Item:

    def __init__(self, name, cost, damage, defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense


class Spell:

    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect


class Effect:

    def __init__(self, damage=0, heal=0, restore=0, defense=0, duration=1):
        self.damage = damage
        self.heal = heal
        self.restore = restore
        self.defense = defense
        self.duration = duration
        self.duration_remaining = duration


SPELLS = [
        Spell('Magic Missile', 53, Effect(damage=4)),
        Spell('Drain', 73, Effect(damage=2, heal=2)),
        Spell('Shield', 113, Effect(defense=7, duration=6)),
        Spell('Poison', 173, Effect(damage=3, duration=6)),
        Spell('Recharge', 229, Effect(restore=101, duration=5))]


class GameOver(Exception):
    pass


class Combat:

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
        self.effects = []

    def do_turn(self):
        # do player turn
        try:
            self.process_effects(self.character1, self.character2)
            self.cast_spell(self.character1)
        except GameOver:
            return self.character2

        # do enemy turn
        self.process_effects(self.character1, self.character2)
        self.attack(self.character2, self.character1)

        #print("Player HP:", self.character1.hit_points,
        #        "Mana:", self.character1.mana)
        #print("Boss HP:", self.character2.hit_points)

        return (
                self.winner(self.character1, self.character2) or
                self.winner(self.character2, self.character1))

    def cast_spell(self, caster):
        #print("Player mana:", caster.mana)

        # Rule out spells already in effect & spells that cost too much
        available_spells = [spell for spell in SPELLS
                if spell.effect not in self.effects and
                caster.mana >= spell.cost]
        #print("Available spells:", [x.name for x in available_spells])

        # If no spells available, game over!
        if not available_spells:
            #print("Could not cast anything!")
            raise GameOver()

        # Choose a spell at random
        spell = random.choice(available_spells)
        #print("Player cast:", spell.name)

        # Decrement caster's mana
        caster.mana -= spell.cost

        # Track caster's total expenditure
        caster.mana_spent += spell.cost

        # Add the effect to effects
        spell.effect.duration_remaining = spell.effect.duration
        self.effects.append(spell.effect)

    def process_effects(self, caster, defender):
        #print("Active effects:")
        for effect in self.effects:
            if effect.duration == effect.duration_remaining:
                caster.temporary_defense += effect.defense

            defender.hit_points -= effect.damage
            caster.hit_points += effect.heal
            caster.mana += effect.restore

            effect.duration_remaining -= 1

            if not effect.duration_remaining:
                caster.temporary_defense -= effect.defense

        self.effects = [x for x in self.effects if x.duration_remaining]

        if caster.hit_points <= 0:
            raise GameOver()

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


def find_least_mana_to_win(hard=False):
    least_mana = float('inf')

    for player, enemy in generate_scenarios(1000000):
        combat = Combat(player, enemy)
        winner = combat.do_full_combat()
        combat.effects = []
        if hard:
            combat.effects = [Effect(heal=-1, duration=float('inf'))]

        if winner == player and player.mana_spent < least_mana:
            least_mana = player.mana_spent

    return least_mana


def generate_scenarios(iterations):
    for i in range(iterations):
        #print("*****")
        player = MagicUser(name='player', hit_points=50, mana=500)
        enemy = Character(name='boss', hit_points=71,
                natural_damage=10, natural_defense=0)

        yield player, enemy


if __name__ == '__main__':
    least_mana = find_least_mana_to_win()
    print("Part 1:", least_mana)

    least_mana = find_least_mana_to_win(hard=True)
    print("Part 2:", least_mana)
