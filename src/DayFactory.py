# src/DayFactory.py

from src.Days.Day1 import Day1
from src.Days.Day2 import Day2
from src.Days.Day3 import Day3
from src.Days.Day4 import Day4

advent_days = {
    'Day1': Day1(),
    'Day2': Day2(),
    'Day3': Day3(),
    'Day4': Day4(),
}


class DayFactory:
    """
    Day Factory class
    """
    @staticmethod
    def instantiate(day_number=0):
        return advent_days["Day" + str(day_number)]
