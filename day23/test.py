#!/usr/bin/env python

import unittest

from day23 import Computer


class TestComputer(unittest.TestCase):

    def setUp(self):
        self.computer = Computer()

    def test_has_registers(self):
        self.assertEqual(self.computer.a, 0)
        self.assertEqual(self.computer.b, 0)

    def test_has_instruction_pointer(self):
        self.assertEqual(self.computer.ip, 0)

    def test_parses_instructions(self):
        instruction, args = self.computer.parse_instruction("hlf a")
        self.assertEqual(instruction, 'hlf')
        self.assertEqual(args, ['a'])

        instruction, args = self.computer.parse_instruction("jio a, +2")
        self.assertEqual(instruction, 'jio')
        self.assertEqual(args, ['a', '+2'])

    def test_executes_hlf(self):
        self.computer.a = 2
        self.computer.ip = 0

        self.computer.hlf('a')
        self.assertEqual(self.computer.a, 1)
        self.assertEqual(self.computer.ip, 1)

    def test_executes_tpl(self):
        self.computer.a = 1
        self.computer.ip = 0

        self.computer.tpl('a')
        self.assertEqual(self.computer.a, 3)
        self.assertEqual(self.computer.ip, 1)

    def test_executes_inc(self):
        self.computer.a = 0
        self.computer.ip = 0

        self.computer.inc('a')
        self.assertEqual(self.computer.a, 1)
        self.assertEqual(self.computer.ip, 1)

    def test_executes_jmp(self):
        self.computer.a = 0
        self.computer.ip = 0

        self.computer.jmp('+3')
        self.assertEqual(self.computer.ip, 3)

        self.computer.jmp('-2')
        self.assertEqual(self.computer.ip, 1)

    def test_executes_jie(self):
        self.computer.a = 2
        self.computer.b = 1
        self.computer.ip = 0

        self.computer.jie('a', '+2')
        self.assertEqual(self.computer.ip, 2)

        self.computer.jie('b', '-2')
        self.assertEqual(self.computer.ip, 3)

    def test_executes_jio(self):
        self.computer.a = 2
        self.computer.b = 1
        self.computer.ip = 0

        self.computer.jio('b', '+2')
        self.assertEqual(self.computer.ip, 2)

        self.computer.jio('a', '-2')
        self.assertEqual(self.computer.ip, 3)

    def test_halts_when_no_more_instructions(self):
        self.computer.a = 0
        self.computer.b = 0
        self.computer.ip = 0

        program = ['inc a', 'inc b', 'inc a']
        self.computer.run_program(program)
        self.assertEqual(self.computer.a, 2)
        self.assertEqual(self.computer.b, 1)
        self.assertEqual(self.computer.ip, 3)



if __name__ == '__main__':
    unittest.main()
