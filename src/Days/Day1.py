# src/Days/Day1.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day1Puzzle1(Puzzle):
    """
    Day1 Puzzle1 class
    """
    def solve(self):
        print("Day1 - Puzzle1")
        stars = self.input.splitlines()

        result = None

        for i in range(0, len(stars)):
            for j in range(i, len(stars)):
                total = int(stars[i]) + int(stars[j])

                if total == 2020:
                    result = int(stars[i]) * int(stars[j])
                    break

        print(f"Solution for Day1 Puzzle1: {result}")


class Day1Puzzle2(Puzzle):
    """
    Day1 Puzzle2 class
    """
    def solve(self):
        print("Day1 - Puzzle2")
        stars = self.input.splitlines()

        result = None

        for i in range(0, len(stars)):
            for j in range(i, len(stars)):
                for k in range(i, len(stars)):
                    total = int(stars[i]) + int(stars[j]) + int(stars[k])

                    if total == 2020:
                        result = int(stars[i]) * int(stars[j]) * int(stars[k])
                        break

        print(f"Solution for Day1 Puzzle2: {result}")


class Day1(Day):
    """
    Day1 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day1, self).__init__(day_number=1)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day1Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day1Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day1.day {}>".format(self.day_number)
