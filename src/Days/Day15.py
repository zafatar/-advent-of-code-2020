# src/Days/Day15.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day15Puzzle1(Puzzle):
    """
    Day15 Puzzle1 class
    """
    def solve(self):
        print("Day15 - Puzzle1")
        numbers = list(map(lambda x: int(x), self.input.splitlines()[0].split(",")))

        # init the stack
        seen = {}
        turn = 0
        last_spoken = 0

        while(turn < 2020):
            turn = turn + 1

            # init the first N element same as the given list
            if turn <= len(numbers):
                last_spoken = numbers[turn - 1]
                seen[last_spoken] = [turn]
                continue

            # decide what to speak based on last_spoken
            if len(seen[last_spoken]) == 1:
                last_spoken = 0
            else:
                last_spoken = seen[last_spoken][-1] - seen[last_spoken][-2]

            # update the list of seen index.
            if last_spoken not in seen:
                seen[last_spoken] = [turn]
            else:
                seen[last_spoken].append(turn)

                # we just need to keep only 2 element in this list.
                if len(seen[last_spoken]) > 2:
                    seen[last_spoken].pop(0)

        result = last_spoken

        print(f"Solution for Day15 Puzzle1: {result}")


class Day15Puzzle2(Puzzle):
    """
    Day15 Puzzle2 class
    """
    def solve(self):
        print("Day15 - Puzzle2")
        numbers = list(map(lambda x: int(x), self.input.splitlines()[0].split(",")))

        # init the stack
        seen = {}
        turn = 0
        last_spoken = 0

        while(turn < 30000000):
            turn = turn + 1

            # init the first N element same as the given list
            if turn <= len(numbers):
                last_spoken = numbers[turn - 1]
                seen[last_spoken] = [turn]
                continue

            # decide what to speak based on last_spoken
            if len(seen[last_spoken]) == 1:
                last_spoken = 0
            else:
                last_spoken = seen[last_spoken][-1] - seen[last_spoken][-2]

            # update the list of seen index.
            if last_spoken not in seen:
                seen[last_spoken] = [turn]
            else:
                seen[last_spoken].append(turn)

                # we just need to keep only 2 element in this list.
                if len(seen[last_spoken]) > 2:
                    seen[last_spoken].pop(0)

        result = last_spoken

        print(f"Solution for Day15 Puzzle1: {result}")


class Day15(Day):
    """
    Day15 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day15, self).__init__(day_number=15)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day15Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day15Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day15.day {}>".format(self.day_number)
