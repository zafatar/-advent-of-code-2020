# src/Days/Day13.py

from src.Days.Day4 import validate_field
from src.Day import Day
from src.Puzzle import Puzzle

from functools import reduce


class Day13Puzzle1(Puzzle):
    """
    Day13 Puzzle1 class
    """
    def solve(self):
        print("Day13 - Puzzle1")
        (arrival_min, buses) = self.input.splitlines()

        bus_ids = list(map(lambda bus_id: int(bus_id), filter(lambda bus_id: bus_id != 'x', buses.split(','))))

        next_minute = int(arrival_min)
        found_bus_id = None

        while(next_minute):
            found_bus_id = None
            # print(next_minute)
            for bus_id in bus_ids:
                if next_minute % bus_id == 0:
                    found_bus_id = bus_id
                    break

            if found_bus_id:
                break

            next_minute = next_minute + 1

        waiting_time = next_minute - int(arrival_min)

        result = waiting_time * found_bus_id

        print(f"Solution for Day13 Puzzle1: {result}")


class Day13Puzzle2(Puzzle):
    """
    Day13 Puzzle2 class

    This problem is being solved with the chinese remainder problem.
    The methods which makes the calculation are taken from :

    https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    """
    @staticmethod
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * Day13Puzzle2.mul_inv(p, n_i) * p
        return sum % prod

    @staticmethod
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    def solve(self):
        print("Day13 - Puzzle2")
        (arrival_min, buses) = self.input.splitlines()

        bus_ids = list(map(
            lambda bus_id: int(bus_id) if bus_id != 'x' else bus_id,
            buses.split(',')))

        valid_bus_ids = dict(map(
            lambda bus_id: (int(bus_id), (-1) * bus_ids.index(bus_id)),
            filter(lambda bus_id: bus_id != 'x', bus_ids)))

        n = list(valid_bus_ids.keys())
        a = list(valid_bus_ids.values())

        result = Day13Puzzle2.chinese_remainder(n, a)

        print(f"Solution for Day13 Puzzle2: {result}")


class Day13(Day):
    """
    Day13 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day13, self).__init__(day_number=13)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day13Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day13Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day13.day {}>".format(self.day_number)
