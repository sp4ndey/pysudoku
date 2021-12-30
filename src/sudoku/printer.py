class GridPrinter:
    def __init__(self, grid):
        self.grid = grid
        self.box_size = grid.box_size

    def __box_row_to_str(self, x, y):
        # join all the numbers on the same row within a box
        cells = [str(self.grid[x][y]) for y in range(y, y + self.box_size)]
        return ' '.join(cells)

    def __row_to_str(self, x):
        # join all numbers on the same row, separated by | after every box
        b = self.box_size
        boxes = [self.__box_row_to_str(x, b * y) for y in range(b)]
        return ' | '.join(boxes)

    def __section_to_str(self, section):
        # join all the rows in a section, i.e. a group of box_size rows
        return '\n'.join(self.__row_to_str(x) for x in range(
            self.box_size * section,
            self.box_size * section + self.box_size
        ))

    def __to_string(self):
        # join all sections, separated by a line of hyphens
        b = self.box_size
        s = self.grid.size

        # two hyphens for each number in the row, just one for the last one
        # two additional hyphens for each box, except the last one
        separator_length = s * 2 - 1 + (b - 1) * 2
        separator = '\n{}\n'.format('-' * separator_length)

        return separator.join(self.__section_to_str(s) for s in range(b))

    def display(self):
        print(self.__to_string())
