import itertools
import math


class Stones:
    """This class represents the pluto stones"""

    def __init__(self, file) -> None:
        self.stone_list = self.read_stones(file)
        self.memoize_bitch = {}

    def read_stones(self, file):
        """Read stones"""
        with open(file, "r", encoding="utf-8") as _file:
            contents = _file.read()
        return [int(s) for s in contents.split(" ")]

    def print_stone_list(self):
        """Print that shit"""
        print("Stones are:")
        for num, stone in enumerate(self.stone_list):
            print(f"Stone: {num}\t{stone}")

    def print_stone_count(self):
        """Lists are too long"""
        print(f"There are {len(self.stone_list)} stones")

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
        new_stones = []
        for stone in self.stone_list:
            if stone == 0:
                new_stones.extend([1])
            elif stone in self.memoize_bitch:
                new_stones.extend(self.memoize_bitch[stone])
            else:
                new_stone = self.evaluate_stone(stone)
                new_stones.extend(new_stone)
                self.memoize_bitch[stone] = new_stone
        self.stone_list = new_stones


# pluto = Stones("Inputs/day11_input.txt")
pluto = Stones("Inputs/day11_example.txt")
pluto.print_stone_list()
# for i in range(1, 7):
for i in range(1, 76):
    print()
    print("==================================")
    print(f"After blink: {i}\n\n")
    pluto.blink()
    # pluto.print_stone_list()
    pluto.print_stone_count()
