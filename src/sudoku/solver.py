import itertools
import time

from printer import GridPrinter


class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.grid_size = self.grid.size
        self.solved = False
        self.counter = 0
        self.time = 0

    def __set(self, x, y, value):
        self.counter += 1
        self.grid[x][y] = value

    def __find_candidates(self, x, y):
        """Find candidates for grid[x][y] by examining all its neighbours"""

        candidates = [True] * 10
        for x1, y1 in itertools.chain(
            self.grid.get_row_coordinates(x),
            self.grid.get_col_coordinates(y),
            self.grid.get_box_coordinates(x, y)
        ):
            candidates[self.grid[x1][y1] - 1] = False

        return [i + 1 for i, candidate in enumerate(candidates) if candidate]

    def __next_coordinate(self, x, y):
        # loop back to front of next line at the end of each line
        return x + (y + 1) // self.grid_size, (y + 1) % self.grid_size

    def __solve(self, x, y):
        if x == self.grid_size:
            return True

        x1, y1 = self.__next_coordinate(x, y)

        # if this is a known value, just go the next one
        if self.grid[x][y] != 0:
            return self.__solve(x1, y1)

        # examine the row, column and box to find suitable candidates
        # then go through that list one-by-one until the right one is found
        candidates = self.__find_candidates(x, y)
        for c in candidates:
            self.__set(x, y, c)
            if self.__solve(x1, y1):
                return True
            self.grid[x][y] = 0
        return False

    def solve(self):
        print('Crunching numbers...')
        start = time.time()
        self.solved = self.__solve(0, 0)
        self.time = time.time() - start

        if self.solved:
            print()
            GridPrinter(self.grid).display()
            print()
            self.print_stats()
            return self.grid
        return None

    def print_stats(self):
        print('Values set: {}'.format(self.counter))
        print('Time taken: {:.2f}s'.format(self.time))
