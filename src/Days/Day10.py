# src/Days/Day10.py

from __future__ import annotations

from src.Day import Day
from src.Puzzle import Puzzle

CACHED_COUNTS = {}


class Day10Puzzle1(Puzzle):
    """
    Day10 Puzzle1 class
    """
    def solve(self):
        print("Day10 - Puzzle1")
        lines = self.input.splitlines()

        # convert all of them to int
        unsorted = [int(x) for x in lines]

        numbers = sorted(unsorted)

        # add 0 as starting point and max + 3 to the list since it's possible.
        numbers.insert(0, 0)
        numbers.append(numbers[-1] + 3)

        diff_of_one = 0
        diff_of_three = 0
        for index in range(len(numbers) - 1):
            if numbers[index + 1] - numbers[index] == 1:
                diff_of_one = diff_of_one + 1

            if numbers[index + 1] - numbers[index] == 3:
                diff_of_three = diff_of_three + 1

        result = diff_of_one * diff_of_three

        print(f"Solution for Day10 Puzzle1: {result}")


def count_branches(value: int = 0, series: list = []) -> int:
    weight = 0

    if value in CACHED_COUNTS:
        return CACHED_COUNTS[value]

    for i in range(1, 4):
        next_value = value + i

        # Find the child and then count the children of it.
        if next_value in series:
            next_index = series.index(next_value)

            child_weight = count_branches(value=next_value,
                                          series=series[next_index:])

            if child_weight == 0:
                weight = 1
            else:
                weight = weight + child_weight

    if value not in CACHED_COUNTS:
        CACHED_COUNTS[value] = weight

    return weight


class Day10Puzzle2(Puzzle):
    """
    Day10 Puzzle2 class
    """
    def solve(self):
        print("Day10 - Puzzle2")
        lines = self.input.splitlines()

        # convert all of them to int
        unsorted = [int(x) for x in lines]

        numbers = sorted(unsorted)

        # add 0 as starting point and max + 3 to the list since it's possible.
        numbers.insert(0, 0)
        numbers.append(numbers[-1] + 3)

        no_of_combinations = count_branches(value=numbers[0], series=numbers[0:])

        print(f"Solution for Day10 Puzzle2: {no_of_combinations}")


class Day10(Day):
    """
    Day10 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day10, self).__init__(day_number=10)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day10Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day10Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day10.day {}>".format(self.day_number)
