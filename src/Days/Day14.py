# src/Days/Day14.py

from src.Day import Day
from src.Puzzle import Puzzle

import re
import itertools


class Day14Puzzle1(Puzzle):
    """
    Day14 Puzzle1 class
    """
    @staticmethod
    def apply_mask(address: int = 0,
                   value: int = 0,
                   mask: str = "",
                   mem: dict = {}) -> str:
        # convert int to binary in the memory
        mem[address] = '{0:036b}'.format(int(value))

        # convert them to the list of 0,1,Xs.
        value_list = list(mem[address])
        mask_list = list(mask)

        for index, bit in enumerate(mask_list):
            if bit == 'X':
                continue

            # mask always wins for 1 and 0.
            value_list[index] = bit

        mem[address] = "".join(value_list)

        return mem

    def solve(self):
        print("Day14 - Puzzle1")
        instructions = self.input.splitlines()

        mem = {}
        curr_mask = None

        for instruction in instructions:
            if instruction.startswith('mem'):
                (address, value) = re.search('^mem\\[(\\d+)\\] = (\\d+)$', instruction).groups()

                # run ops with current mask.
                mem = Day14Puzzle1.apply_mask(address=int(address),
                                              value=int(value),
                                              mask=curr_mask,
                                              mem=mem)

            elif instruction.startswith('mask'):
                curr_mask = re.search('^mask = ([X01]+)$', instruction).groups()[0]
            else:
                print("invalid instructions")

        result = 0
        for value in mem.values():
            result = result + int(value, 2)

        print(f"Solution for Day14 Puzzle1: {result}")


class Day14Puzzle2(Puzzle):
    """
    Day14 Puzzle2 class
    """
    @staticmethod
    def apply_mask(address: int = 0,
                   value: int = 0,
                   mask: str = "",
                   mem: dict = {},
                   initial_value: int = 0) -> str:
        # convert address int to binary in the memory
        binary_address = '{0:036b}'.format(int(address))

        binary_address_as_list = list(binary_address)
        mask_list = list(mask)

        for index, bit in enumerate(mask_list):
            if bit == '0':
                continue

            # mask always wins for 1 or X.
            binary_address_as_list[index] = bit

        Xs = list(filter(lambda x: x == 'X', binary_address_as_list))

        # calculate all combination for X cases.
        binary_combinations = list(itertools.product([0, 1], repeat=len(Xs)))
        for combination in binary_combinations:
            combination_index = 0
            tmp_address_list = binary_address_as_list.copy()

            # Replace all X in the series with the combination values.
            for index, tmp_value in enumerate(tmp_address_list):
                if tmp_value == 'X':
                    tmp_address_list[index] = str(combination[combination_index])
                    combination_index = combination_index + 1

            # build new mem address and convert it to int.
            mem_address = "".join(tmp_address_list)
            mem_address = int(mem_address, 2)

            # update the value in the memory for calculated mem address.
            mem[mem_address] = value

        return mem

    def solve(self):
        print("Day14 - Puzzle2")
        instructions = self.input.splitlines()

        mem = {}
        curr_mask = None

        for instruction in instructions:
            if instruction.startswith('mem'):
                (address, value) = re.search('^mem\\[(\\d+)\\] = (\\d+)$', instruction).groups()

                # run ops with current mask.
                mem = Day14Puzzle2.apply_mask(address=int(address),
                                              value=int(value),
                                              mask=curr_mask,
                                              mem=mem)

            elif instruction.startswith('mask'):
                curr_mask = re.search('^mask = ([X01]+)$', instruction).groups()[0]
            else:
                print("invalid instructions")

        result = 0
        for value in mem.values():
            result = result + value

        print(f"Solution for Day14 Puzzle2: {result}")


class Day14(Day):
    """
    Day14 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day14, self).__init__(day_number=14)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day14Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day14Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day14.day {}>".format(self.day_number)
