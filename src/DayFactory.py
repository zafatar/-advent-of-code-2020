# src/DayFactory.py

from src.Days.Day1 import Day1
from src.Days.Day2 import Day2
from src.Days.Day3 import Day3
from src.Days.Day4 import Day4
from src.Days.Day5 import Day5
from src.Days.Day6 import Day6
from src.Days.Day7 import Day7
from src.Days.Day8 import Day8
from src.Days.Day9 import Day9
from src.Days.Day10 import Day10
from src.Days.Day11 import Day11
from src.Days.Day12 import Day12
from src.Days.Day13 import Day13
from src.Days.Day14 import Day14
from src.Days.Day15 import Day15
from src.Days.Day16 import Day16

advent_days = {
    'Day1': Day1(),
    'Day2': Day2(),
    'Day3': Day3(),
    'Day4': Day4(),
    'Day5': Day5(),
    'Day6': Day6(),
    'Day7': Day7(),
    'Day8': Day8(),
    'Day9': Day9(),
    'Day10': Day10(),
    'Day11': Day11(),
    'Day12': Day12(),
    'Day13': Day13(),
    'Day14': Day14(),
    'Day15': Day15(),
    'Day16': Day16(),
}


class DayFactory:
    """
    Day Factory class
    """
    @staticmethod
    def instantiate(day_number=0):
        return advent_days["Day" + str(day_number)]
