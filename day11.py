import itertools
from copy import deepcopy

"""Day 11
1. If the stone is engraved with the number 0, it is replaced by a stone 
   engraved with the number 1.
2. If the stone is engraved with a number that has an even number of digits,
   it is replaced by two stones. The left half of the digits are engraved on
   the new left stone, and the right half of the digits are engraved on the
   new right stone. (The new numbers don't keep extra leading zeroes: 1000
   would become stones 10 and 0.)
3. If none of the other rules apply, the stone is replaced by a new stone;
the old stone's number multiplied by 2024 is engraved on the new stone.
"""


class Stones:
    """This class represents the pluto stones"""

    def __init__(self, file) -> None:
        self.stone_list = self.read_stones(file)

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
        len_of_stone = len(str(stone))
        # rule 1
        if stone == 0:
            return [1]
        # rule 2
        if len_of_stone % 2 == 0:
            left_stone = int(str(stone)[0 : int(len_of_stone / 2)])
            right_stone = int(str(stone)[int(len_of_stone / 2) :])
            return [left_stone, right_stone]
        return [stone * 2024]

    def blink(self):
        """During blink, process rules for each stone"""
        for ix, stone in enumerate(self.stone_list):
            _stone = self.stone_list.pop(ix)
            self.stone_list.insert(ix, self.evaluate_stone(_stone))
        self.stone_list = list(itertools.chain.from_iterable(self.stone_list))


pluto = Stones("Inputs/day11_input.txt")
# pluto = Stones("Inputs/day11_example.txt")
pluto.print_stone_list()
# for i in range(1, 7):
for i in range(1, 26):
    print()
    print("==================================")
    print(f"After blink: {i}\n\n")
    pluto.blink()
    # pluto.print_stone_list()
    pluto.print_stone_count()
