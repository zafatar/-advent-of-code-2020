# src/Days/Day5.py

from src.Day import Day
from src.Puzzle import Puzzle


def get_seat_id(boarding_pass: str) -> int:
    """This method returns the seat ID by calculating from boarding pass.

    Args:
        boarding_pass (str): Boarding pass string

    Returns:
        int: seat ID
    """
    # normalize to binary
    boarding_pass = boarding_pass.replace('L', '0')
    boarding_pass = boarding_pass.replace('R', '1')
    boarding_pass = boarding_pass.replace('F', '0')
    boarding_pass = boarding_pass.replace('B', '1')

    # convert to 10s.
    row_id = int(boarding_pass[0:7], 2)
    col_id = int(boarding_pass[7:10], 2)

    seat_id = (row_id * 8) + col_id

    return seat_id


def get_sorted_seats(boarding_passes: list = []) -> list:
    """This method returns the sorted list of the seat IDs found from boarding passes.

    Args:
        boarding_passes (list, optional): list of boarding passes. Defaults to [].

    Returns:
        list: sorted list of the seat IDs.
    """
    seats = []
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass=boarding_pass)
        seats.append(seat_id)

    sorted_seats = sorted(seats)

    return sorted_seats


class Day5Puzzle1(Puzzle):
    """
    Day5 Puzzle1 class
    """
    def solve(self):
        print("Day5 - Puzzle1")
        boarding_passes = self.input.splitlines()

        seats = []
        for boarding_pass in boarding_passes:
            seat_id = get_seat_id(boarding_pass=boarding_pass)
            seats.append(seat_id)

        sorted_seats = sorted(seats)

        print(f"Solution for Day5 Puzzle1: {sorted_seats[-1]}")


class Day5Puzzle2(Puzzle):
    """
    Day5 Puzzle2 class
    """
    def solve(self):
        print("Day5 - Puzzle2")
        boarding_passes = self.input.splitlines()

        seats = []
        for boarding_pass in boarding_passes:
            seat_id = get_seat_id(boarding_pass=boarding_pass)
            seats.append(seat_id)

        sorted_seats = sorted(seats)

        # find the missing seat in the sorted list.
        my_seat_id = None
        for index in range(sorted_seats[0], sorted_seats[-1]):
            if index not in sorted_seats:
                my_seat_id = index

        print(f"Solution for Day5 Puzzle2: {my_seat_id}")


class Day5(Day):
    """
    Day5 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day5, self).__init__(day_number=5)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day5Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day5Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day5.day {}>".format(self.day_number)
