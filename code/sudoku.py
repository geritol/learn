"""
Sudoku solver.
---------------
Input: 2D puzzle array, with the value 0 representing an unknown square.
Returns *a* solution to the sudoku, or None if the sudoku cannot be solved.

improvments will be needed:
- check validity of sudoku's
- refine get_valid_moves method to look for single occurences of number within rows, columns, big squares
"""


from itertools import chain
from copy import deepcopy


class Sudoku:

    def __init__(self, initial_board):
        self.valid_nums = [i for i in range(1, 10)]
        self.shortest_decision_point = [0, 0]
        self.shortest_decision_length = 9
        self.board = deepcopy(initial_board)
        self.flipped = [[row[i] for row in self.board] for i in range(len(self.board))]
        self.boxes = [list(chain.from_iterable([self.board[i // 3 * 3 + sub][i % 3 * 3: i % 3 * 3 + 3] for sub in range(3)])) for i in range(len(self.board))]
        self.is_valid = True
        self.valid_moves = self.get_valid_moves()
        self.solution = self.solve()

    @property
    def is_solved(self):
        return self.is_valid and False not in [0 not in line for line in self.board]

    @staticmethod
    def _box_index_from_coords(x, y):
        row = x // 3 * 3
        col = y // 3
        return row + col

    def get_valid_moves(self):
        if not self.is_valid: return
        board = deepcopy(self.board)

        # iterate over rows
        for i in range(len(self.board)):
            # iterate over numbers in rows
            for j in range(len(self.board[i])):
                num = self.board[i][j]
                if num != 0: continue
                box_index = self._box_index_from_coords(i, j)
                possibilities = list(set(self.valid_nums) - set(self.board[i]) - set(self.flipped[j]) - set(self.boxes[box_index]))

                if len(possibilities) == 0:
                    self.is_valid = False
                    return None
                else:
                    board[i][j] = possibilities
                    if len(possibilities) < self.shortest_decision_length:
                        self.shortest_decision_point=[i,j]
                        self.shortest_decision_length = len(possibilities)
                    if len(possibilities) == 1:
                        return board
        return board

    def solve(self):
        if self.is_solved:
            return self.board
        elif not self.is_valid:
            return None
        else:
            options = self.valid_moves[self.shortest_decision_point[0]][self.shortest_decision_point[1]]
            for option in options:
                next_board = self.board[:]
                next_board[self.shortest_decision_point[0]][self.shortest_decision_point[1]] = option
                res = Sudoku(next_board).solution
                if res: return res
            return None


problem = \
[[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]

# hardest sudoku?
# from http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html

hard = \
 [[8, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 3, 6, 0, 0, 0, 0, 0],
 [0, 7, 0, 0, 9, 0, 2, 0, 0],
 [0, 5, 0, 0, 0, 7, 0, 0, 0],
 [0, 0, 0, 0, 4, 5, 7, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 3, 0],
 [0, 0, 1, 0, 0, 0, 0, 6, 8],
 [0, 0, 8, 5, 0, 0, 0, 1, 0],
 [0, 9, 0, 0, 0, 0, 4, 0, 0]]

# claimed to be solved by his alog in 188.79 sec
# http://norvig.com/sudoku.html
hard2 = \
[[0, 0, 0, 0, 0, 6, 0, 0, 0],
 [0, 5, 9, 0, 0, 0, 0, 0, 8],
 [2, 0, 0, 0, 0, 8, 0, 0, 0],
 [0, 4, 5, 0, 0, 0, 0, 0, 0],
 [0, 0, 3, 0, 0, 0, 0, 0, 0],
 [0, 0, 6, 0, 0, 3, 0, 5, 4],
 [0, 0, 0, 3, 2, 5, 0, 0, 6],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 0.01 secs for norvig
hard3 = \
 [[0, 0, 5, 3, 0, 0, 0, 0, 0],
 [8, 0, 0, 0, 0, 0, 0, 2, 0],
 [0, 7, 0, 0, 1, 0, 5, 0, 0],
 [4, 0, 0, 0, 0, 5, 3, 0, 0],
 [0, 1, 0, 0, 7, 0, 0, 0, 6],
 [0, 0, 3, 2, 0, 0, 0, 8, 0],
 [0, 6, 0, 5, 0, 0, 0, 0, 9],
 [0, 0, 4, 0, 0, 0, 0, 3, 0],
 [0, 0, 0, 0, 0, 9, 7, 0, 0]]

print(Sudoku(hard3).solution)
