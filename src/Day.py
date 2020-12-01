# src/Day.py

import os


class Day:
    """
    Base class for the Day
    """
    day_number = 0
    puzzles = []
    input_folder = None

    def __init__(self, day_number=0):
        """
        Class constructor
        """
        self.day_number = day_number
        self.input_folder = self.build_input_folder()

    def puzzle(self, puzzle=0):
        pass

    def build_input_folder(self):
        app_dir_path = os.path.dirname(os.path.realpath(__file__))
        return "{}/../inputs/{}".format(app_dir_path, str(self.day_number).rjust(2, '0'))

    def __repr__(self):
        return "<Day.day {}>".format(self.number)
