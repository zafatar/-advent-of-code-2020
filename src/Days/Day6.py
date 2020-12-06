# src/Days/Day6.py

from src.Day import Day
from src.Puzzle import Puzzle


class Group(object):
    answers = {}
    no_of_people = 0

    def __init__(self, answers: dict = {}, no_of_people: int = 0):
        self.answers = answers
        self.no_of_people = no_of_people


def get_groups(lines: list = []) -> list:
    """This method returns the list of groups

    Args:
        lines (list, optional): [description]. Defaults to [].

    Returns:
        list: [description]
    """
    # collect all the groups by:
    # - keeping each group in a dict
    # - starting a new group after each empty line
    # - building the key values with a split on column
    groups = []
    curr_group = Group(answers={}, no_of_people=0)
    for line in lines:

        if line == '':
            groups.append(curr_group)
            curr_group = Group(answers={}, no_of_people=0)
        else:
            curr_group.no_of_people = curr_group.no_of_people + 1

            attrs = list(line)
            for attr in attrs:
                if attr not in curr_group.answers:
                    curr_group.answers[attr] = 1

                else:
                    curr_group.answers[attr] = curr_group.answers[attr] + 1
                    # print(curr_group.answers[attr])

    # since we skip the last line, we add the last group manually.
    groups.append(curr_group)

    return groups


class Day6Puzzle1(Puzzle):
    """
    Day6 Puzzle1 class
    """
    def solve(self):
        print("Day6 - Puzzle1")
        lines = self.input.splitlines()

        groups = get_groups(lines=lines)

        total_answers = 0
        for group in groups:
            print(group.answers)
            total_answers = total_answers + len(group.answers.keys())

        print(f"Solution for Day6 Puzzle1: {total_answers}")


class Day6Puzzle2(Puzzle):
    """
    Day6 Puzzle2 class
    """
    def solve(self):
        print("Day6 - Puzzle2")
        lines = self.input.splitlines()

        groups = get_groups(lines=lines)

        questions_answered_by_everbody = 0
        for group in groups:
            no_of_people = group.no_of_people

            for answer in group.answers.keys():
                if group.answers[answer] == no_of_people:
                    questions_answered_by_everbody = questions_answered_by_everbody + 1

        print(f"Solution for Day6 Puzzle2: {questions_answered_by_everbody}")


class Day6(Day):
    """
    Day6 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day6, self).__init__(day_number=6)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day6Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day6Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day6.day {}>".format(self.day_number)
