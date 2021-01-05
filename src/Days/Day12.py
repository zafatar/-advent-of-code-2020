# src/Days/Day122.py

from __future__ import annotations

from src.Day import Day
from src.Puzzle import Puzzle

import re

DIRECTIONS = ['N', 'E', 'S', 'W']   # Clockwise


class Point:
    x = 0
    y = 0
    face = ''

    def __init__(self, x: int = 0, y: int = 0, face: str = None) -> Point:
        self.x = x
        self.y = y
        self.face = face

    def __repr__(self) -> str:
        return f'{self.x} x {self.y} : {self.face}'


class Day12Puzzle1(Puzzle):
    """
    Day12 Puzzle1 class
    """
    def solve(self):
        print("Day12 - Puzzle1")
        instructions = self.input.splitlines()

        curr_point = Point(x=0, y=0, face='E')

        for instruction in instructions:
            (direction, move) = re.search('([NSEWFLR])(\\d+)', instruction).groups()

            if direction == 'N':
                curr_point.y = curr_point.y + int(move)
            elif direction == 'S':
                curr_point.y = curr_point.y - int(move)
            elif direction == 'E':
                curr_point.x = curr_point.x + int(move)
            elif direction == 'W':
                curr_point.x = curr_point.x - int(move)
            elif direction == 'L':
                no_of_turn = int(move) / 90
                index_of_direction = DIRECTIONS.index(curr_point.face)
                index_of_new_direction = int((index_of_direction - no_of_turn) % 4)

                curr_point.face = DIRECTIONS[index_of_new_direction]

            elif direction == 'R':
                no_of_turn = int(move) / 90
                index_of_direction = DIRECTIONS.index(curr_point.face)
                index_of_new_direction = int((index_of_direction + no_of_turn) % 4)

                curr_point.face = DIRECTIONS[index_of_new_direction]

            elif direction == 'F':
                if curr_point.face == 'N':
                    curr_point.y = curr_point.y + int(move)
                elif curr_point.face == 'S':
                    curr_point.y = curr_point.y - int(move)
                elif curr_point.face == 'E':
                    curr_point.x = curr_point.x + int(move)
                elif curr_point.face == 'W':
                    curr_point.x = curr_point.x - int(move)

        result = abs(curr_point.x) + abs(curr_point.y)

        print(f"Solution for Day12 Puzzle1: {result}")


class Day12Puzzle2(Puzzle):
    """
    Day12 Puzzle2 class
    """
    def solve(self):
        print("Day12 - Puzzle2")
        instructions = self.input.splitlines()

        curr_point = Point(x=0, y=0, face='E')
        # The waypoint starts 10 units east and 1 unit north relative to the ship.
        waypoint = Point(x=curr_point.x + 10, y=curr_point.y + 1, face='E')

        for instruction in instructions:
            (direction, move) = re.search('([NSEWFLR])(\\d+)', instruction).groups()

            if direction == 'N':
                waypoint.y = waypoint.y + int(move)
            elif direction == 'S':
                waypoint.y = waypoint.y - int(move)
            elif direction == 'E':
                waypoint.x = waypoint.x + int(move)
            elif direction == 'W':
                waypoint.x = waypoint.x - int(move)
            elif direction == 'L' or direction == 'R':
                no_of_turn = int(move) / 90

                x_diff = waypoint.x - curr_point.x
                y_diff = waypoint.y - curr_point.y

                # L90 = R270
                if (direction == 'L' and no_of_turn == 1) or (direction == 'R' and no_of_turn == 3):
                    waypoint.x = curr_point.x - y_diff
                    waypoint.y = curr_point.y + x_diff
                # R90 = L270
                elif (direction == 'L' and no_of_turn == 3) or (direction == 'R' and no_of_turn == 1):
                    waypoint.x = curr_point.x + y_diff
                    waypoint.y = curr_point.y - x_diff
                # L180 = R180
                elif no_of_turn == 2:
                    waypoint.x = curr_point.x - x_diff
                    waypoint.y = curr_point.y - y_diff

            elif direction == 'F':
                x_diff = waypoint.x - curr_point.x
                y_diff = waypoint.y - curr_point.y

                curr_point.x = curr_point.x + (int(move) * x_diff)
                curr_point.y = curr_point.y + (int(move) * y_diff)

                waypoint.x = curr_point.x + x_diff
                waypoint.y = curr_point.y + y_diff

        result = abs(curr_point.x) + abs(curr_point.y)

        print(f"Solution for Day12 Puzzle2: {result}")


class Day12(Day):
    """
    Day12 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day12, self).__init__(day_number=12)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day12Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day12Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day12.day {}>".format(self.day_number)
