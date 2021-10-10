# src/Days/Day16.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day16Puzzle1(Puzzle):
    """
    Day16 Puzzle1 class
    """

    def _read_ticket(self, line: str = None) -> "list[int]":
        ticket = list(map(lambda x: int(x), line.split(",")))
        return ticket

    def solve(self):
        print("Day16 - Puzzle1")
        lines = self.input.splitlines()

        # Read the valid rules_for_ticket_fields,
        # your ticket and nearby tickets.
        rules_for_ticket_fields = {}
        # your_ticket = []
        nearby_tickets = []
        read_nearby_tickets = False
        for index, line in enumerate(lines):
            # rules_for_ticket_fields.
            if ': ' in line:
                (section, numbers) = line.split(': ')
                rules_for_ticket_fields[section] = list(
                    map(lambda x: x.split('-'), numbers.split(' or ')))

            # if 'your ticket' in line:
            #     your_ticket = self._read_ticket(lines[index+1])

            if 'nearby tickets' in line:
                read_nearby_tickets = True
                continue

            if read_nearby_tickets:
                nearby_ticket = self._read_ticket(line)
                nearby_tickets.append(nearby_ticket)

        not_valid_numbers = []
        for nearby_ticket in nearby_tickets:
            for number in nearby_ticket:
                number_valid = False
                for _, intervals in rules_for_ticket_fields.items():
                    for interval in intervals:
                        if int(interval[0]) <= number <= int(interval[1]):
                            number_valid = True

                if not number_valid:
                    not_valid_numbers.append(number)

        # ticket scanning error rate
        result = sum(not_valid_numbers)

        print(f"Solution for Day16 Puzzle1: {result}")


class Day16Puzzle2(Puzzle):
    """
    Day16 Puzzle2 class
    """
    def _read_ticket(self, line: str = None) -> "list[int]":
        ticket = list(map(lambda x: int(x), line.split(",")))
        return ticket

    @staticmethod
    def _get_columns(valid_tickets: list = [], column: int = 0):
        return list(map(lambda x: x[column], valid_tickets))

    @staticmethod
    def _get_valid_tickets(nearby_tickets: list = [],
                           rules_for_ticket_fields: dict = {}):
        valid_tickets = []

        for nearby_ticket in nearby_tickets:
            is_ticket_valid = True
            for number in nearby_ticket:
                number_valid = False
                for _, intervals in rules_for_ticket_fields.items():
                    for interval in intervals:
                        if int(interval[0]) <= number <= int(interval[1]):
                            number_valid = True

                if not number_valid:
                    is_ticket_valid = False

            if is_ticket_valid:
                valid_tickets.append(nearby_ticket)

        return valid_tickets

    def solve(self):
        print("Day16 - Puzzle2")
        lines = self.input.splitlines()

        # Read the valid rules_for_ticket_fields,
        # your ticket and nearby tickets.
        rules_for_ticket_fields = {}
        your_ticket = []
        nearby_tickets = []
        read_nearby_tickets = False
        for index, line in enumerate(lines):
            # rules_for_ticket_fields.
            if ': ' in line:
                (section, numbers) = line.split(': ')
                rules_for_ticket_fields[section] = list(
                    map(lambda x: x.split('-'), numbers.split(' or ')))

            if 'your ticket' in line:
                your_ticket = self._read_ticket(lines[index+1])

            if 'nearby tickets' in line:
                read_nearby_tickets = True
                continue

            if read_nearby_tickets:
                nearby_ticket = self._read_ticket(line)
                nearby_tickets.append(nearby_ticket)

        # find the valid tickets.
        valid_tickets = Day16Puzzle2.\
            _get_valid_tickets(nearby_tickets,
                               rules_for_ticket_fields)

        # collect the stats per role and per valid ticket column value
        stats = {}
        for rule, intervals in rules_for_ticket_fields.items():
            for col in range(len(your_ticket)):
                valid_ticket_values = Day16Puzzle2._get_columns(
                    valid_tickets, col)

                if rule not in stats.keys():
                    stats[rule] = {}

                # Count the valid column numbers for each column.
                for number in valid_ticket_values:
                    if int(intervals[0][0]) <= number <= int(intervals[0][1]) or \
                            int(intervals[1][0]) <= number <= int(intervals[1][1]):
                        if col not in stats.get(rule):
                            stats.get(rule)[col] = 1
                        else:
                            stats[rule][col] = stats[rule][col] + 1

                # Keep only the ones which have full match
                # with all valid tickets, the rest will be deleted.
                if stats[rule][col] != len(valid_tickets):
                    del stats[rule][col]

        # sort stats by the length of possible items
        match_rules = {}
        allocated = []
        sorted_stats = sorted(stats.items(), key=lambda item: len(item[1]))
        for rule, potential_columns in sorted_stats:
            possible_column_ids = list(potential_columns.keys())

            # Get the diff of possible ids and already allocated ones.
            matched_id = list(set(possible_column_ids) - set(allocated))[0]
            # register the matched columnd id to the alreayd allocated list.
            allocated.append(matched_id)

            # map the rule with the matched id.
            match_rules[rule] = matched_id

        # calculate the result from your ticket by finding the numbers
        # for the rules starting with `departure`
        result = 1
        for rule, column_id in match_rules.items():
            if rule.startswith("departure"):
                result = result * your_ticket[column_id]

        print(f"Solution for Day16 Puzzle2: {result}")


class Day16(Day):
    """
    Day16 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day16, self).__init__(day_number=16)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day16Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day16Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day16.day {}>".format(self.day_number)
