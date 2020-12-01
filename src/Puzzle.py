# src/Puzzle.py

import os


class Puzzle:
    """
    Puzzle class
    """
    puzzle_number = 0
    input = None

    def __init__(self, puzzle_number=0, day_number=None):
        self.puzzle_number = puzzle_number
        self.day_number = day_number
        self.input = self.read_input_file_content()

    def read_input_file_content(self):
        """
        :return: content of the input file for the puzzle
        """
        app_dir_path = os.path.dirname(os.path.realpath(__file__))
        input_folder = "{}/../inputs/{}".format(app_dir_path, str(self.day_number).rjust(2, '0'))

        input_file = "{}/{}".format(input_folder, self.puzzle_number)

        # TODO: Check if the file exists
        file = open(input_file, "r")
        return file.read()

    def solve(self):
        pass
