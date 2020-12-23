# src/Days/Day11.py

from __future__ import annotations

from src.Day import Day
from src.Puzzle import Puzzle

from copy import deepcopy


class Grid:
    width = 0
    height = 0
    cells = {}

    def __init__(self, rows: list = [], extended: bool = False) -> Grid:
        # Build the grid with cells
        for x in range(len(rows)):
            row = list(rows[x])

            for y in range(len(row)):
                cell = Cell(x=x, y=y, value=row[y])

                if x not in self.cells:
                    self.cells[x] = {}

                self.cells[x][y] = cell

        # Set the width and height of the grid.
        self.width = len(self.cells.keys())
        self.height = len(self.cells[0].keys())

        # calculate adjacent cells coordinates for each cell.
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]

                if extended:
                    self.cells[x][y].adjacent_cells = self._extended_adjacent_cells(cell=cell)
                else:
                    self.cells[x][y].adjacent_cells = self._adjacent_cells(cell=cell)

    def _adjacent_cells(self, cell: Cell) -> list:
        adjacent_cells = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= cell.x + i < self.width and \
                    0 <= cell.y + j < self.height and (i != 0 or j != 0):

                    # collect adjacent cell coordinates as tuple.
                    adjacent_cells.append((cell.x + i, cell.y + j))

        return adjacent_cells

    def _extended_adjacent_cells(self, cell: Cell) -> list:
        adjacent_cells = []

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for c in range(1, self.width):
                    if 0 <= cell.x + (i * c) < self.width and \
                        0 <= cell.y + (j * c) < self.height and (i != 0 or j != 0):

                        # adjacent cell coorditaes.
                        adjacent_cell_x = cell.x + (i * c)
                        adjacent_cell_y = cell.y + (j * c)

                        # collect it if it's a seat i.e. not floor.
                        if self.cells[adjacent_cell_x][adjacent_cell_y].value != '.':
                            adjacent_cells.append(
                                (adjacent_cell_x, adjacent_cell_y)
                            )
                            break

        return adjacent_cells

    def occupied_adjacent_cells(self, cell: Cell) -> int:
        occupied_adjacent_cells = 0

        for (x, y) in cell.adjacent_cells:
            if self.cells[x][y].value == '#':
                occupied_adjacent_cells = occupied_adjacent_cells + 1

        return occupied_adjacent_cells

    def count_occupied_seats(self) -> int:
        occupied_seats = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y].value == '#':
                    occupied_seats = occupied_seats + 1

        return occupied_seats

    def loop_grid_cells(self, extended: bool = False):
        seat_changed = True
        loop_count = 0

        while(seat_changed):
            seat_changed = False
            grid_cells = self.cells
            grid_cells_to_be_updated = deepcopy(grid_cells)

            for x in range(len(self.cells)):
                for y in range(len(self.cells[x])):
                    current_cell = self.cells[x][y]

                    if current_cell.value == 'L':
                        occupied_adjacent_seats = self.occupied_adjacent_cells(cell=current_cell)

                        if occupied_adjacent_seats == 0:
                            seat_changed = True
                            grid_cells_to_be_updated[x][y].value = '#'

                    elif current_cell.value == '#':
                        occupied_adjacent_seats = self.occupied_adjacent_cells(cell=current_cell)

                        occupied_adjacent_condition = 4
                        if extended:
                            occupied_adjacent_condition = 5

                        if occupied_adjacent_seats >= occupied_adjacent_condition:
                            seat_changed = True
                            grid_cells_to_be_updated[x][y].value = 'L'

                    else:
                        pass

            if seat_changed:
                self.cells = grid_cells_to_be_updated

            loop_count = loop_count + 1

        occupied_seats = self.count_occupied_seats()

        return occupied_seats

    def __repr__(self) -> str:
        grid = ''
        for x in range(self.width):
            for y in range(self.height):
                grid = grid + self.cells[x][y].value
            grid = grid + '\n'
        return grid


class Cell:
    x = 0
    y = 0
    value = ''
    adjacent_cells = []

    def __init__(self, x: int = 0, y: int = 0, value: str = None) -> Cell:
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self) -> str:
        return f'{self.x} x {self.y} : {self.value} > {self.adjacent_cells}'


class Day11Puzzle1(Puzzle):
    """
    Day11 Puzzle1 class
    """
    def solve(self):
        print("Day11 - Puzzle1")
        rows = self.input.splitlines()

        # starting grid
        grid = Grid(rows=rows, extended=False)
        occupied_seats = grid.loop_grid_cells()

        print(f"Solution for Day11 Puzzle1: {occupied_seats}")


class Day11Puzzle2(Puzzle):
    """
    Day11 Puzzle2 class
    """
    def solve(self):
        print("Day11 - Puzzle2")
        rows = self.input.splitlines()

        # starting grid
        grid = Grid(rows=rows, extended=True)
        occupied_seats = grid.loop_grid_cells(extended=True)

        print(f"Solution for Day11 Puzzle1: {occupied_seats}")


class Day11(Day):
    """
    Day11 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day11, self).__init__(day_number=11)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day11Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day11Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day11.day {}>".format(self.day_number)
