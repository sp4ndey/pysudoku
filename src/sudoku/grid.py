import copy
import itertools
import math


class Grid:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.size = len(grid)
        self.box_size = math.isqrt(self.size)

    def __getitem__(self, row):
        return self.grid[row]

    def get_row_coordinates(self, row):
        return itertools.product([row], range(self.size))

    def get_col_coordinates(self, col):
        return itertools.product(range(self.size), [col])

    def get_box_coordinates(self, row, col):
        s = self.box_size
        return itertools.product(
            range(s * (row // s), s * (row // s) + s),
            range(s * (col // s), s * (col // s) + s)
        )
