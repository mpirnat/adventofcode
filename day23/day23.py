#!/usr/bin/env python

"""
Solve day 23 of Advent of Code.

http://adventofcode.com/day/23
"""

class Computer:

    def __init__(self):
        """
        Our computer has 2 registers, a and b,
        and an instruction pointer so that we know
        which instruction to fetch next.
        """
        self.a = 0
        self.b = 0
        self.ip = 0     # Ye olde instruction pointer

    def run_program(self, program):
        """
        Run a list of program instructions until we
        try to move the instruction pointer beyond
        the bounds of the instruction list.
        """
        while True:
            try:
                instruction, args = self.parse_instruction(program[self.ip])
            except IndexError:
                return
            getattr(self, instruction)(*args)

    def parse_instruction(self, line):
        """
        Parse a line of the program into
        the instruction and its arguments.
        """
        instruction, *args = line.strip().replace(',', '').split()
        return instruction, args

    def hlf(self, register):
        """
        Set the register to half its current value,
        then increment the instruction pointer.
        """
        setattr(self, register, getattr(self, register)//2)
        self.ip += 1

    def tpl(self, register):
        """
        Set the register to triple its current value,
        then increment the instruction pointer.
        """
        setattr(self, register, getattr(self, register)*3)
        self.ip += 1

    def inc(self, register):
        """
        Increment the value in the register,
        then increment the instruction pointer.
        """
        setattr(self, register, getattr(self, register) + 1)
        self.ip += 1

    def jmp(self, offset):
        """
        Jump the instruction pointer by a particular offset.
        """
        self.ip += int(offset)

    def jie(self, register, offset):
        """
        Jump the instruction pointer by an offset
        if the value in the register is even.
        """
        if getattr(self, register) % 2 == 0:
            self.jmp(offset)
        else:
            self.ip += 1

    def jio(self, register, offset):
        """
        Jump the instruction pointer by an offset
        if the value in the register is one.
        """
        if getattr(self, register) == 1:
            self.jmp(offset)
        else:
            self.ip += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        program = f.readlines()
        computer = Computer()

        # Part 1 - start with a=0, b=0
        computer.run_program(program)
        print("Part 1:", computer.b)

        # Part 2 - now start with a=1, b=0
        computer = Computer()
        computer.a = 1
        computer.run_program(program)
        print("Part 2:", computer.b)
