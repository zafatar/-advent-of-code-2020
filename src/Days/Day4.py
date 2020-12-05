# src/Days/Day4.py

from src.Day import Day
from src.Puzzle import Puzzle

import re

# Mandatory field check list.
MANDATORY_PASSPORT_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]


def get_passports(lines: list = []) -> list:
    """This method returns the list of passports

    Args:
        lines (list, optional): [description]. Defaults to [].

    Returns:
        list: [description]
    """
    # collect all the passports by:
    # - keeping each passort in a dict
    # - starting a new passport after each empty line
    # - building the key values with a split on column
    passports = []
    curr_passport = {}
    for line in lines:
        if len(passports) == 0 or line == '':
            if line == '':
                passports.append(curr_passport)
                curr_passport = {}
        else:
            attrs = line.split(' ')
            for attr in attrs:
                (key, value) = attr.split(':')
                curr_passport[key] = value

    # since we skip the last line, we add the last passport manually.
    passports.append(curr_passport)

    return passports


def validate_field(field: str = None, value: str = None) -> bool:

    if (field == 'byr' and 1920 <= int(value) and int(value) <= 2002):
        return True

    if (field == 'iyr' and 2010 <= int(value) and int(value) <= 2020):
        return True

    if (field == 'eyr' and 2020 <= int(value) and int(value) <= 2030):
        return True

    if (field == 'hgt') and re.search(r'(\d+)(in|cm)', value):
        (height, unit) = re.search(r'(\d+)(in|cm)', value).groups()
        if (unit == 'cm' and 150 <= int(height) and int(height) <= 193) or \
           (unit == 'in' and 59 <= int(height) and int(height) <= 76):
            return True

    if (field == 'hcl') and re.search(r'#[0-9a-f]{6}', value):
        return True

    if (field == 'ecl' and re.search(r'(amb|blu|brn|gry|grn|hzl|oth)', value)):
        return True

    if (field == 'pid') and re.search(r'^[0-9]{9}$', value):
        return True

    return False


class Day4Puzzle1(Puzzle):
    """
    Day4 Puzzle1 class
    """
    def solve(self):
        print("Day4 - Puzzle1")
        lines = self.input.splitlines()

        passports = get_passports(lines=lines)

        valid_passports = 0
        for passport in passports:
            mandatory_fields_number = len(MANDATORY_PASSPORT_FIELDS)
            for field in MANDATORY_PASSPORT_FIELDS:
                if field in passport:
                    mandatory_fields_number = mandatory_fields_number - 1

            if mandatory_fields_number == 0:
                valid_passports = valid_passports + 1

        print(f"Solution for Day4 Puzzle1: {valid_passports}")


class Day4Puzzle2(Puzzle):
    """
    Day4 Puzzle2 class
    """
    def solve(self):
        print("Day4 - Puzzle2")
        lines = self.input.splitlines()

        passports = get_passports(lines=lines)

        valid_passports = 0
        for passport in passports:
            mandatory_fields_number = len(MANDATORY_PASSPORT_FIELDS)
            for field in MANDATORY_PASSPORT_FIELDS:
                if field in passport and \
                    validate_field(field=field, value=passport[field]):
                    mandatory_fields_number = mandatory_fields_number - 1

            if mandatory_fields_number == 0:
                valid_passports = valid_passports + 1

        print(f"Solution for Day4 Puzzle2: {valid_passports}")


class Day4(Day):
    """
    Day4 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day4, self).__init__(day_number=4)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day4Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day4Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day4.day {}>".format(self.day_number)
