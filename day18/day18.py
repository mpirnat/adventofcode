#!/usr/bin/env python

"""
Solve day 18 of Advent of Code.

http://adventofcode.com/day/18

"""

import pprint


def make_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('.')
        board.append(row)
    return board


def initialize_board(config):
    board = [list(x.strip()) for x in config.split()]
    return board


def next_board(board):
    new_board = make_board(len(board), len(board[0]))
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            num_neighbors_on = neighbors_on(board, i, j)
            new_board[i][j] = ('#'
                    if (cell == '#' and num_neighbors_on in (2, 3)) or
                        (cell == '.' and num_neighbors_on == 3)
                    else '.')
    return new_board


def next_board_pt2(board):
    new_board = make_board(len(board), len(board[0]))
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            num_neighbors_on = neighbors_on(board, i, j)
            new_board[i][j] = ('#'
                    if (i == 0 and j == 0) or
                        (i == 0 and j == len(board[0])-1) or
                        (i == len(board)-1 and j == 0) or
                        (i == len(board)-1 and j == len(board[0])-1) or
                        (cell == '#' and num_neighbors_on in (2, 3)) or
                        (cell == '.' and num_neighbors_on == 3)
                    else '.')
    return new_board


def neighbors_on(board, row, col):
    rows = [row-1, row, row+1]
    cols = [col-1, col, col+1]

    count = 0

    for i in rows:

        if i < 0 or i >= len(board[0]):
            continue

        for j in cols:

            if j < 0 or j >= len(board):
                continue

            # skip the current cell
            if i == row and j == col:
                continue
            try:
                on = board[i][j] == '#'
            except IndexError:
                pass
            else:
                count += 1 if on else 0

    return count


def count_lights_on(board):
    return sum([row.count('#') for row in board])


if __name__ == '__main__':
    with open('input.txt') as f:
        initial_state = f.read()
        """
        board = initialize_board(initial_state)
        for i in range(100):
            board = next_board(board)
        print("Part 1:", count_lights_on(board))
        """

        board = initialize_board(initial_state)
        for i in range(100):
            board = next_board_pt2(board)
        print("Part 2:", count_lights_on(board))
