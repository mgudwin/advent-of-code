"""Imports"""

import copy
import math
from collections import defaultdict


class Stones:
    """This class represents the pluto stones"""

    def __init__(self, file) -> None:
        self.stone_dict = self.read_stones_to_dict(file)
        self.memoized_dict = defaultdict(int)

    def read_stones_to_dict(self, file):
        """Read stones"""
        d = defaultdict(int)
        with open(file, "r", encoding="utf-8") as _file:
            contents = _file.read()
        for stone in [int(s) for s in contents.split(" ")]:
            d[stone] = 1
        return d

    def print_stones(self):
        """Print that shit"""
        print("Stones are:")
        for key in self.stone_dict:
            print(f"Stone: {key:<30} : {self.stone_dict[key]}")

    def evaluate_stone(self, stone):
        """Process rules"""
        # rule 1
        if stone == 0:
            return [1]
        # rule 2
        len_of_stone = int(math.log10(stone)) + 1
        if len_of_stone % 2 == 0:
            left_stone = stone // 10 ** (len_of_stone // 2)
            right_stone = stone % 10 ** (len_of_stone // 2)
            return [left_stone, right_stone]
        return [stone * 2024]

    def blink(self):
        """During blink, process rules for each stone"""
        d = copy.deepcopy(self.stone_dict)
        for key in copy.deepcopy(d):
            _count = d[key]
            if self.memoized_dict[key]:
                for _stone in self.memoized_dict[key]:
                    d[_stone] += _count
            else:
                for _stone in self.evaluate_stone(key):
                    d[_stone] += _count
            if d[key] == _count:
                del d[key]
            else:
                d[key] -= _count
            # d[key] -= _count
        self.stone_dict = d

    def sum_stones(self):
        """Get sum"""
        _sum = 0
        for key in self.stone_dict:
            _sum += self.stone_dict[key]
        print(f"There are now {_sum} stones")

    def process_blinks(self, blink_count, debug_output):
        """Combined"""
        for i in range(blink_count + 1):
            print(f"==================================\nAfter blink: {i}")
            self.blink()
            self.sum_stones()
            if debug_output:
                self.print_stones()


pluto = Stones("Inputs/day11_input.txt")
# pluto = Stones("Inputs/day11_example.txt")
pluto.process_blinks(blink_count=75, debug_output=False)
