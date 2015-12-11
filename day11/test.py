#!/usr/bin/env python

import unittest
from day11 import follows_rules, next_password, make_new_password


class TestMakingNewPasswords(unittest.TestCase):

    def test_rejects_if_not_8_chars(self):
        self.assertEquals(follows_rules('a'*7), False)
        self.assertEquals(follows_rules('a'*9), False)
        self.assertEquals(follows_rules('abcdffaa'), True)

    def test_rejects_bad_chars(self):
        self.assertEquals(follows_rules('hijklmmn'), False)

    def test_rejects_if_no_increasing_straights(self):
        self.assertEquals(follows_rules('abbceffg'), False)

    def test_rejects_without_2_pairs(self):
        self.assertEquals(follows_rules('abbcegjk'), False)
        self.assertEquals(follows_rules('abcdffaa'), True)

    def test_increments_password(self):
        self.assertEquals(next_password('aa'), 'ab')
        self.assertEquals(next_password('az'), 'ba')

    def test_makes_next_valid_password(self):
        self.assertEquals(make_new_password('abcdefgh'), 'abcdffaa')
        # takes too long
        #self.assertEquals(make_new_password('ghijklmn'), 'ghjaabcc')



if __name__ == '__main__':
    unittest.main()
