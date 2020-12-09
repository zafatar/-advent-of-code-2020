# src/Days/Day8.py

from __future__ import annotations

from src.Day import Day
from src.Puzzle import Puzzle

import re
from copy import deepcopy


class Command(object):
    action = 'acc'
    operator = '+'
    value = 0
    execution_count = 0

    def __init__(self, action: str = 'acc', operator: str = '+', value: int = 0) -> Command:
        self.action = action
        self.operator = operator
        self.value = value
        self.execution_count = 0

    def __repr__(self) -> str:
        return f'{self.action} => {self.operator} {self.value} : {self.execution_count}'


def get_commands(instructions: list = []) -> list:
    """[summary]

    Args:
        instructions (list, optional): list of instructions. Defaults to [].

    Returns:
        list: list of command in order of instructions
    """
    commands = []
    for instruction in instructions:
        (action, direction) = instruction.split()
        (operator, value) = re.search(r'^([+-])(\d+)$', direction).groups()

        command = Command(action=action, operator=operator, value=int(value))

        commands.append(command)

    return commands


def loop_commands(commands: list) -> tuple(bool, int):
    """This method loops the given command list and returns 2 values.
    First one is a boolean which holds the flag if command chain is infinite.
    Second one is the accumulator value in the chain.

    Args:
        commands (list): list of commands

    Returns:
        [tuple(bool, int)]: Flag for infinity of the commands and last known accumulator value
    """
    is_infinite = True
    accumulator = 0
    curr_index = 0
    curr_command = commands[curr_index]

    while(curr_command.execution_count == 0):
        # increase the execution count by 1.
        curr_command.execution_count = curr_command.execution_count + 1

        if curr_command.action == 'acc':
            if curr_command.operator == '+':
                accumulator = accumulator + int(curr_command.value)
            elif curr_command.operator == '-':
                accumulator = accumulator - int(curr_command.value)
            else:
                print(f'Unexpected operator: {curr_command.operator}')

            curr_index = curr_index + 1

        elif curr_command.action == 'jmp':

            if curr_command.operator == '+':
                curr_index = curr_index + int(curr_command.value)
            elif curr_command.operator == '-':
                curr_index = curr_index - int(curr_command.value)
            else:
                print(f'Unexpected operator: {curr_command.operator}')

        elif curr_command.action == 'nop':

            # do nothing and get the next one.
            curr_index = curr_index + 1

        else:
            print(f'Unexpected instruction code: {curr_command.operator}')

        # if index is out of bound.
        if 0 <= curr_index and curr_index < len(commands):
            curr_command = commands[curr_index]
        else:
            is_infinite = False
            break

    return (is_infinite, accumulator)


class Day8Puzzle1(Puzzle):
    """
    Day8 Puzzle1 class
    """
    def solve(self):
        print("Day8 - Puzzle1")
        instructions = self.input.splitlines()

        commands = get_commands(instructions=instructions)

        (is_infinite, accumulator) = loop_commands(commands=commands)

        print(f"Solution for Day8 Puzzle1: {accumulator}")


class Day8Puzzle2(Puzzle):
    """
    Day8 Puzzle2 class
    """
    def solve(self):
        print("Day8 - Puzzle2")
        instructions = self.input.splitlines()

        commands = get_commands(instructions=instructions)

        last_accumulator = None
        for index in range(len(commands)):
            c = commands[index]

            if c.action == 'nop' or c.action == 'jmp':
                # clone the commands and keep the originals.
                clone_commands = deepcopy(commands)

                if c.action == 'nop':
                    clone_commands[index].action = 'jmp'
                elif c.action == 'jmp':
                    clone_commands[index].action = 'nop'

                (is_infinite, accumulator) = loop_commands(commands=clone_commands)

                if not is_infinite:
                    last_accumulator = accumulator
                    break

        print(f"Solution for Day8 Puzzle2: {last_accumulator}")


class Day8(Day):
    """
    Day8 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day8, self).__init__(day_number=8)

    def puzzle(self, puzzle_number=8):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day8Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day8Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day8.day {}>".format(self.day_number)
