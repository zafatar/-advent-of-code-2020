# src/Days/Day2.py

from src.Day import Day
from src.Puzzle import Puzzle

import re


class Day2Puzzle1(Puzzle):
    """
    Day2 Puzzle1 class
    """
    def solve(self):
        print("Day2 - Puzzle1")
        lines = self.input.splitlines()

        valid_pwds = 0

        for line in lines:
            (min, max, char, empty_string, password) = re.split('[\s\-:]', line)
            min = int(min)
            max = int(max)

            # count the occurence of each char.
            password_dict = dict()
            for w in password:
                if w in password_dict.keys():
                    password_dict[w] = password_dict[w]+1
                else:
                    password_dict[w] = 1

            if char in password_dict.keys():
                if min <= password_dict[char] and password_dict[char] <= max:
                    valid_pwds = valid_pwds + 1

        print(f"Solution for Day2 Puzzle1: {valid_pwds}")


class Day2Puzzle2(Puzzle):
    """
    Day2 Puzzle2 class
    """
    def solve(self):
        print("Day2 - Puzzle2")
        lines = self.input.splitlines()

        valid_pwds = 0

        for line in lines:
            (min, max, char, empty_string, password) = re.split('[\s\-:]', line)
            min = int(min)
            max = int(max)

            valid_pos = 0
            if password[min - 1] == char:
                valid_pos = valid_pos + 1

            if password[max - 1] == char:
                valid_pos = valid_pos + 1

            if valid_pos == 1:
                valid_pwds = valid_pwds + 1

        print(f"Solution for Day2 Puzzle2: {valid_pwds}")


class Day2(Day):
    """
    Day2 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day2, self).__init__(day_number=2)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day2Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day2Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day2.day {}>".format(self.day_number)
