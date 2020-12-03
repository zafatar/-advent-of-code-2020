# src/Days/Day3.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day3Point(object):
    x = 0
    y = 0

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{__class__.__name__}: x: {self.x} y: {self.y}'


def init_map(input: str = None):
    lines = input.splitlines()

    geo_map = []
    for line in lines:
        geo_map.append(list(line))

    return geo_map


def count_trees_by_map(geo_map: dict = [],
                       slope: list = [],
                       curr_point: Day3Point = None) -> int:
    trees = 0
    while(curr_point.y < len(geo_map)):
        # check the area, count the trees.
        if geo_map[curr_point.y][curr_point.x] == '#':
            trees = trees + 1

        # move to the next point.
        next_x = (curr_point.x + slope[0]) % len(geo_map[curr_point.y])
        next_y = curr_point.y + slope[1]

        curr_point = Day3Point(x=next_x, y=next_y)

    return trees


class Day3Puzzle1(Puzzle):
    """
    Day3 Puzzle1 class
    """
    def solve(self):
        print("Day3 - Puzzle1")

        # build matrix map
        geo_map = init_map(input=self.input)

        # init starting point
        curr_point = Day3Point()

        trees = count_trees_by_map(geo_map=geo_map,
                                   slope=(3, 1),
                                   curr_point=curr_point)

        print(f"Solution for Day3 Puzzle1: {trees}")


class Day3Puzzle2(Puzzle):
    """
    Day3 Puzzle2 class
    """
    def solve(self):
        print("Day3 - Puzzle2")

        # build matrix map
        geo_map = init_map(input=self.input)

        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        result = 1
        for slope in slopes:
            # init starting point
            curr_point = Day3Point()
            trees = count_trees_by_map(geo_map=geo_map,
                                       slope=slope,
                                       curr_point=curr_point)

            print(f'Slope: {slope[0]} - {slope[1]} : {trees}')
            result = result * trees

        print(f"Solution for Day3 Puzzle2: {result}")


class Day3(Day):
    """
    Day3 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day3, self).__init__(day_number=3)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day3Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day3Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day3.day {}>".format(self.day_number)
