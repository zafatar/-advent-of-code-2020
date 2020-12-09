# src/Days/Day9.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day9Puzzle1(Puzzle):
    """
    Day9 Puzzle1 class
    """
    def solve(self):
        print("Day9 - Puzzle1")
        lines = self.input.splitlines()

        # convert all of them to int
        numbers = [int(x) for x in lines]

        PRE = 25
        first_not_valid = None
        for index in range(PRE, len(numbers)):
            valid_number = numbers[index]

            slice_min = index - PRE
            slice_max = index
            prev_seq = numbers[slice_min:slice_max]

            is_valid = False
            for i in range(0, len(prev_seq)):
                for j in range(i, len(prev_seq)):
                    total = int(prev_seq[i]) + int(prev_seq[j])
                    if i != j and total == valid_number:
                        is_valid = True

                    if is_valid:
                        break

            if not is_valid:
                first_not_valid = valid_number
                break

        print(f"Solution for Day9 Puzzle1: {first_not_valid}")


class Day9Puzzle2(Puzzle):
    """
    Day9 Puzzle2 class
    """
    def solve(self):
        print("Day9 - Puzzle2")
        lines = self.input.splitlines()

        # convert all of them to int
        numbers = [int(x) for x in lines]

        SUM = 258585477
        # find the index of this int in the list.
        sum_index = 0
        for index in range(0, len(numbers)):
            if numbers[index] == SUM:
                sum_index = index
                break

        # by decrasing the index from sum index
        # find the proper sequence whose sum is SUM
        curr_seq = None
        for index in reversed(range(0, sum_index)):
            for seq_min_index in range(0, index):
                # get the sequence with the min and max index.
                seq = numbers[sum_index-seq_min_index:index]

                # calculate the sum and check if it's the wanted one.
                seq_sum = sum(seq)
                if seq_sum == SUM:
                    curr_seq = seq
                    break

        # sort the sequence to get the min and the max values.
        sorted_curr_seq = sorted(curr_seq)

        total = sorted_curr_seq[0] + sorted_curr_seq[-1]

        print(f"Solution for Day9 Puzzle2: {total}")


class Day9(Day):
    """
    Day9 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day9, self).__init__(day_number=9)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day9Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day9Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day9.day {}>".format(self.day_number)
