import argparse
from grid import Grid
from solver import SudokuSolver


def main():
    parser = argparse.ArgumentParser(description='Solve a Sudoku grid.')
    parser.add_argument(
        '-f',
        '--file',
        dest='filename',
        help='Input file containing the grid to solve'
    )

    args = parser.parse_args()

    grid = []
    if args.filename:
        with open(args.filename) as fin:
            for line in fin:
                grid.append([int(c) for c in line.rstrip('\n')])
    else:
        print('Enter the Sudoku grid to solve:')
        for _ in range(9):
            line = input()
            grid.append([int(c) for c in line.rstrip('\n')])
        print()

    solver = SudokuSolver(Grid(grid))
    solver.solve()


if __name__ == "__main__":
    main()
