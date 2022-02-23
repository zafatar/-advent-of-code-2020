# src/Days/Day19.py

from typing import Tuple

from src.Day import Day
from src.Puzzle import Puzzle


class Day19Puzzle1(Puzzle):
    """
    Day19 Puzzle1 class
    """
    rules = {}

    def _read_rules_and_texts(self, lines: list = []) -> Tuple[dict, list]:
        rules = {}
        texts = []

        for line in lines:
            if len(line) > 0:
                if line[0].isdigit():
                    (rule_number, rule) = line.split(": ")
                    rules[int(rule_number)] = rule.replace('"', '').split(" ")
                else:
                    texts.append(line)

        return rules, texts

    def loop_rule(rules: dict = {}, rule_id: int = None):
        rule = rules.get(rule_id)
        print(rule)

        # if rule_id == 0:
        regex = ""

        for index in rule:
            # print(f"Index: {index}")
            if index == 'a' or index == 'b':
                regex = regex + index
            else:
                regex = Day19Puzzle1.loop_rule(rules, rule_id=int(index))

        return regex

    def print_rule(rules: dict = {}, rule_id: int = None):
        print(rules.get(rule_id))

    @staticmethod
    def match(text, rule):
        return True

    @staticmethod
    def gen_regex(rules={}):
        pass

    def solve(self):
        print("Day19 - Puzzle1")
        lines = self.input.splitlines()

        (rules, texts) = self._read_rules_and_texts(lines)

        for rule_id, rule in sorted(rules.items()):
            print(f'{rule_id} - {rule}')

        regex = Day19Puzzle1.loop_rule(rules, rule_id=0)
        print(regex)

        result = 0
        # for text in texts:
        #     if Day19Puzzle1.match(text=text, rule=rules[0]):
        #         result = result + 1

        print(f"Solution for Day19 Puzzle1: {result}")


class Day19Puzzle2(Puzzle):
    """
    Day19 Puzzle2 class
    """
    def solve(self):
        print("Day19 - Puzzle2")
        lines = self.input.splitlines()

        # init the stack
        result = None

        print(f"Solution for Day19 Puzzle1: {result}")


class Day19(Day):
    """
    Day19 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day19, self).__init__(day_number=19)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day19Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day19Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day19.day {}>".format(self.day_number)
