# src/Days/Day7.py

from __future__ import annotations

from src.Day import Day
from src.Puzzle import Puzzle

import re


class Bag(object):
    name = None
    contains = []

    def __init__(self, name: str = None) -> None:
        self.name = name
        self.contains = []

    def get_parents(self, bags: dict) -> list:
        """[summary]

        Args:
            bags (dict): bags dict, bag names as key.

        Returns:
            list: list of parents bag of given bag
        """
        parent_bags = []

        for bag_name in bags.keys():
            parent_bag = bags.get(bag_name)
            for child_bag_block in parent_bag.contains:
                if child_bag_block.get('bag').name == self.name:
                    parent_bags.append(parent_bag)

        return parent_bags

    def __repr__(self) -> str:
        return f'<Bag Name: {self.name}>'


def get_bags(instructions: list) -> dict:
    """This returns the list of bags with the instance of bag and their contain lists.

    Args:
        lines (list): list of inot instruction lines.

    Returns:
        list: dict of the bags, bag name as the key.
    """
    bags = {}

    for ins in instructions:
        (bag_name, ingredients) = ins.split('contain')
        bag_name = bag_name.replace(' bags', '').strip()

        if bag_name not in bags:
            bag = Bag(name=bag_name)
            bags[bag_name] = bag

        ingredients = ingredients.replace('.', '').strip()
        ingredients = ingredients.split(', ')
        for ingredient in ingredients:
            ingredient = ingredient.replace(' bags', '').replace(' bag', '').strip()

            if re.search('^(\d+) (.*)$', ingredient):
                (number, child_bag_name) = re.search('^(\d+) (.*)$', ingredient).groups()

                if child_bag_name not in bags:
                    child_bag = Bag(name=child_bag_name)
                    bags[child_bag_name] = child_bag

                contain = {
                    'count': int(number),
                    'bag': bags[child_bag_name]
                }

                bags[bag_name].contains.append(contain)
            else:
                pass    # no child bags.

    return bags


def count_parent_bags(bag_name: str, bags: dict, parents: dict = {}) -> int:
    """Count the parent bags of the given bag with a recursive approach.

    Args:
        bag_name (str): name of the bag whose parents to be counted
        bags (dict): all bags map as dict
        parents (dict, optional): already collected parents. Defaults to {}.

    Returns:
        int: no of bags as parents
    """
    bag = bags[bag_name]

    if bag.get_parents(bags=bags) != []:
        child_parents = bag.get_parents(bags=bags)

        for parent in child_parents:
            parents = count_parent_bags(bag_name=parent.name,
                                        bags=bags,
                                        parents=parents)

            if parent.name not in parents:
                parents[parent.name] = 1
            else:
                parents[parent.name] = parents[parent.name] + 1

    else:
        if bag_name not in parents:
            parents[bag_name] = 1
        else:
            parents[bag_name] = parents[bag_name] + 1

    return parents


def count_children_bags(bag_name: str, bags: dict) -> int:
    """[summary]

    Args:
        bag_name (str): name of the bag whose children to be counted
        bags (dict): all bags map as dict
        children (list): [description]

    Returns:
        int: no of bags as children
    """
    bag = bags[bag_name]
    count = 0

    if bag.contains != []:
        for child_bag in bag.contains:
            child_count = child_bag.get('count')
            count = count + (
                child_count + (
                    child_count * count_children_bags(child_bag.get('bag').name, bags=bags)
                )
            )

    return count


class Day7Puzzle1(Puzzle):
    """
    Day7 Puzzle1 class
    """
    def solve(self):
        print("Day7 - Puzzle1")
        instructions = self.input.splitlines()

        bags = get_bags(instructions=instructions)

        my_bag_name = 'shiny gold'
        containers = count_parent_bags(bag_name=my_bag_name, bags=bags, parents={})

        # 115
        print(f"Solution for Day7 Puzzle1: {len(containers.keys())}")


class Day7Puzzle2(Puzzle):
    """
    Day7 Puzzle2 class
    """
    def solve(self):
        print("Day7 - Puzzle2")
        instructions = self.input.splitlines()

        bags = get_bags(instructions=instructions)

        my_bag_name = 'shiny gold'
        containers = count_children_bags(bag_name=my_bag_name, bags=bags)

        print(f"Solution for Day7 Puzzle2: {containers}")


class Day7(Day):
    """
    Day7 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day7, self).__init__(day_number=7)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day7Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day7Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day7.day {}>".format(self.day_number)
