# src/Days/Day18.py

from src.Day import Day
from src.Puzzle import Puzzle

MULTIPLICATION = '*'
SUM = '+'
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Day18Puzzle1(Puzzle):
    """
    Day18 Puzzle1 class
    """
    def calculate(items: list = []):
        res = None

        if '(' in items:
            open_index = 0

            for index in range(len(items)):
                if items[index] == '(':
                    open_index = index
                    continue

                elif items[index] == ')':
                    sub_items = items[open_index+1: index]
                    res = Day18Puzzle1.calculate_block(sub_items)

                    # build new items
                    new_items = []
                    for a in items[0:open_index]:
                        new_items.append(a)

                    new_items.append(res)

                    for b in items[index+1:]:
                        new_items.append(b)

                    res = Day18Puzzle1.calculate(items=new_items)
                    break
        else:
            res = Day18Puzzle1.calculate_block(items)

        return res

    def calculate_block(items: list = []):
        result = None

        if len(items) == 1:
            return items[0]

        if items[1] == MULTIPLICATION:
            result = items[0] * items[2]
        elif items[1] == SUM:
            result = items[0] + items[2]

        items = items[3:]
        items.insert(0, result)

        # Calculate the new items.
        result = Day18Puzzle1.calculate_block(items)

        return result

    def solve(self):
        print("Day18 - Puzzle1")
        lines = self.input.splitlines()

        result = 0
        for line in lines:
            formula = list(map(
                lambda x: int(x) if x in NUMBERS else str(x),
                filter(lambda x: x != ' ', list(line))))

            res = Day18Puzzle1.calculate(items=formula)
            # print(f"Items: {formula} Res: {res}")

            result = result + res

        print(f"Solution for Day18 Puzzle1: {result}")


class Day18Puzzle2(Puzzle):
    """
    Day18 Puzzle2 class
    """
    def calculate(items: list = []):
        res = None

        if '(' in items:
            open_index = 0

            for index in range(len(items)):
                if items[index] == '(':
                    open_index = index
                    continue

                elif items[index] == ')':
                    sub_items = items[open_index+1: index]
                    res = Day18Puzzle2.calculate_block(sub_items)

                    # build new items
                    new_items = []
                    for a in items[0:open_index]:
                        new_items.append(a)

                    new_items.append(res)

                    for b in items[index+1:]:
                        new_items.append(b)

                    res = Day18Puzzle2.calculate(items=new_items)
                    break
        else:
            res = Day18Puzzle2.calculate_block(items)

        return res

    def calculate_block(items: list = []):
        result = None

        index = 1
        while (SUM in items):
            if items[index] == SUM:
                result = items[index-1] + items[index+1]

                items[index] = result
                del items[index+1]
                del items[index-1]
                index = 1
            else:
                if len(items) > 3:
                    index = index + 2

        while (MULTIPLICATION in items):
            if items[index] == MULTIPLICATION:
                result = items[index-1] * items[index+1]

                items[index] = result
                del items[index+1]
                del items[index-1]
                index = 1
            else:
                if len(items) > 3:
                    index = index + 2

        result = items[0]

        return result

    def solve(self):
        print("Day18 - Puzzle2")
        lines = self.input.splitlines()

        result = 0
        for line in lines:
            formula = list(map(
                lambda x: int(x) if x in NUMBERS else str(x),
                filter(lambda x: x != ' ', list(line))))

            res = Day18Puzzle2.calculate(items=formula)

            # sum the results to overall one.
            result = result + res

        print(f"Solution for Day18 Puzzle1: {result}")


class Day18(Day):
    """
    Day18 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day18, self).__init__(day_number=18)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day18Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day18Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day18.day {}>".format(self.day_number)
