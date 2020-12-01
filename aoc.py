# migrate.py

import argparse

from src.DayFactory import DayFactory

parser = argparse.ArgumentParser(description='Advent of Code solutions')
parser.add_argument("-d", "--day", help="day of the problem and solutions", type=int)
parser.add_argument("-p", "--puzzle", help="puzzle number, 1 or 2", type=int)

args = parser.parse_args()

if __name__ == '__main__':
    day = DayFactory.instantiate(day_number=args.day)
    puzzle = day.puzzle(puzzle_number=args.puzzle)
    puzzle.solve()
