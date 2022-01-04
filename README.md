# PySudoku
## Usage
    $ python3 src/sudoku/sudoku.py -f sample_boards/very_hard_3
    Crunching numbers...

    7 8 4 | 2 9 5 | 3 1 6
    2 6 9 | 8 1 3 | 4 5 7
    3 5 1 | 4 7 6 | 9 8 2
    ---------------------
    4 3 2 | 7 6 8 | 1 9 5
    8 9 6 | 5 2 1 | 7 4 3
    5 1 7 | 3 4 9 | 2 6 8
    ---------------------
    9 7 3 | 6 5 4 | 8 2 1
    1 2 5 | 9 8 7 | 6 3 4
    6 4 8 | 1 3 2 | 5 7 9

    Values set: 158097
    Time taken: 1.85s

    $ python3 src/sudoku/sudoku.py < sample_boards/very_hard_3
    Enter the Sudoku grid to solve:

    Crunching numbers...

    7 8 4 | 2 9 5 | 3 1 6
    2 6 9 | 8 1 3 | 4 5 7
    3 5 1 | 4 7 6 | 9 8 2
    ---------------------
    4 3 2 | 7 6 8 | 1 9 5
    8 9 6 | 5 2 1 | 7 4 3
    5 1 7 | 3 4 9 | 2 6 8
    ---------------------
    9 7 3 | 6 5 4 | 8 2 1
    1 2 5 | 9 8 7 | 6 3 4
    6 4 8 | 1 3 2 | 5 7 9

    Values set: 158097
    Time taken: 1.80s

    $ python3 src/sudoku/sudoku.py
    Enter the Sudoku grid to solve:
    080000010
    060003000
    301070900
    402008090
    000500700
    010000000
    903004020
    000080004
    600000000

    Crunching numbers...

    7 8 4 | 2 9 5 | 3 1 6
    2 6 9 | 8 1 3 | 4 5 7
    3 5 1 | 4 7 6 | 9 8 2
    ---------------------
    4 3 2 | 7 6 8 | 1 9 5
    8 9 6 | 5 2 1 | 7 4 3
    5 1 7 | 3 4 9 | 2 6 8
    ---------------------
    9 7 3 | 6 5 4 | 8 2 1
    1 2 5 | 9 8 7 | 6 3 4
    6 4 8 | 1 3 2 | 5 7 9

    Values set: 158097
    Time taken: 1.73s
