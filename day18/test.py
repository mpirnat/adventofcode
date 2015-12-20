#!/usr/bin/env python

import unittest

from day18 import make_board
from day18 import initialize_board
from day18 import next_board, next_board_pt2
from day18 import count_lights_on


class TestAnimatingLights(unittest.TestCase):

    rows = 6
    cols = 6

    initial_state = \
""".#.#.#
...##.
#....#
..#...
#.#..#
####.."""

    step_1 = \
"""..##..
..##.#
...##.
......
#.....
#.##.."""

    step_2 = \
"""..###.
......
..###.
......
.#....
.#...."""

    step_3 = \
"""...#..
......
...#..
..##..
......
......"""

    step_4 = \
"""......
......
..##..
..##..
......
......"""


    def test_creates_board(self):
        board = make_board(self.rows, self.cols)
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 6)
        self.assertEqual(board[0], ['.'] * 6)

    def test_initializes_board(self):
        board = initialize_board(self.initial_state)
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 6)
        self.assertEqual(board[0], list('.#.#.#'))
        self.assertEqual(board[1], list('...##.'))

    def test_advances_board(self):
        board = initialize_board(self.initial_state)

        board = next_board(board)
        self.assertEqual(board, initialize_board(self.step_1))

        board = next_board(board)
        self.assertEqual(board, initialize_board(self.step_2))

        board = next_board(board)
        self.assertEqual(board, initialize_board(self.step_3))

        board = next_board(board)
        self.assertEqual(board, initialize_board(self.step_4))

    def test_counts_lights_on(self):
        board = initialize_board(self.initial_state)
        self.assertEqual(count_lights_on(board), 15)


class TestAnimatingLightsWithStuckCorners(unittest.TestCase):

    initial_state = \
"""##.#.#
...##.
#....#
..#...
#.#..#
####.#"""

    step_1 = \
"""#.##.#
####.#
...##.
......
#...#.
#.####"""

    step_2 = \
"""#..#.#
#....#
.#.##.
...##.
.#..##
##.###"""

    step_3 = \
"""#...##
####.#
..##.#
......
##....
####.#"""

    step_4 = \
"""#.####
#....#
...#..
.##...
#.....
#.#..#"""

    step_5 = \
"""##.###
.##..#
.##...
.##...
#.#...
##...#"""

    def test_advances_board(self):
        board = initialize_board(self.initial_state)

        board = next_board_pt2(board)
        self.assertEqual(board, initialize_board(self.step_1))

        board = next_board_pt2(board)
        self.assertEqual(board, initialize_board(self.step_2))

        board = next_board_pt2(board)
        self.assertEqual(board, initialize_board(self.step_3))

        board = next_board_pt2(board)
        self.assertEqual(board, initialize_board(self.step_4))

        board = next_board_pt2(board)
        self.assertEqual(board, initialize_board(self.step_5))


if __name__ == '__main__':
    unittest.main()
