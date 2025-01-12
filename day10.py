from collections import deque

# from typing import List
from copy import deepcopy

from tabulate import tabulate

# Can only move up, down, left, right
# trailhead starts at 0 and scored by however many 9s you can reaach from it
# TODO: Can use tuples instead of list to represent current point and then you
# can store them in dictionary directly as keys without having to str() it
# TODO: Can also consider using a set instead of a dict for visited when you're
# only tracking "is this in here or not"
# TODO: For pt2 consider that you can't end up in a loop because valid paths
# increase by 1 each time so you could never loop back around because by definition
# that would be a smaller number than you're on


class Map:
    """Class for map object"""

    def __init__(self, file):
        with open(file, "r", encoding="utf-8") as _file:
            contents = _file.read()
        rows = contents.strip().split("\n")
        self.map = [list(x) for x in rows]
        self.map = [[int(char) for char in row] for row in self.map]
        self.ncols = len(self.map)
        self.nrows = len(self.map[0])
        self.headers = [str(i) for i in range(self.ncols)]
        self.print_map(self.map)
        self.trailheads = self.find_trailheads()

    def print_map(self, _map):
        """Print out map"""
        print("Printing map...")
        print(tabulate(_map, tablefmt="plain", headers=self.headers, showindex=True))

    def find_trailheads(self):
        """Find trailhead locations"""
        trailhead_map = deepcopy(self.map)
        list_of_trailheads = []
        for row in range(len(trailhead_map)):
            for col in range(len(trailhead_map[0])):
                if trailhead_map[row][col] == 0:
                    list_of_trailheads.append((row, col))
        return list_of_trailheads

    def print_trailhead_list(self):
        "Print trailhead list"
        print("List of trailheads in [row, col] format are:")
        for trailhead in self.trailheads:
            print(f"{trailhead}")

    def process_trailhead(self, trailhead_loc: list):
        """Process the trailhead"""
        queue = deque()
        nines = []
        visited = []
        visited.append(trailhead_loc)
        queue.append(trailhead_loc)
        neighbors = []
        while queue:
            curr_point = queue.popleft()
            curr_value = self.map[curr_point[0]][curr_point[1]]
            neighbors = self.get_neighbors(curr_point)
            # print(neighbors)
            for neighbor in neighbors:
                # print("Processing neighbor", neighbor)
                neighbor_value = self.map[neighbor[0]][neighbor[1]]
                if neighbor_value == curr_value + 1:
                    if neighbor_value == 9:
                        nines.append(str(neighbor))
                    if str(neighbor) not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        nines = list(set(nines))
        print(f"These are the visited locations\n{visited}\n")
        return nines

    def get_neighbors(self, current_point):
        """Function to get neighbors for point"""
        neighbors = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir in directions:
            c = [current_point[0] + dir[0], current_point[1] + dir[1]]
            if self.check_bounds(c):
                neighbors.append(c)
        return neighbors

    def check_bounds(self, point):
        """Function to check if point is in bound"""
        return (
            point[0] >= 0
            and point[1] >= 0
            and point[0] < self.nrows
            and point[1] < self.ncols
        )

    def process_all_trailheads(self):
        """Function to process all trailheads on map"""
        peaks = []
        score = 0
        for trailhead in self.trailheads:
            # print("Processing trailhead {}".format(trailhead))
            new_peaks = self.process_trailhead(trailhead)
            _score = len(new_peaks)
            # print("Score for this trailhead is {}".format(_score))
            peaks += new_peaks
            score += _score
        # print("There are {} Peaks".format(len(peaks)))
        print(f"Total score is {score}")
        # print("Here are all the peaks:\n", peaks)


# INPUT_FILE = "Inputs/day10_input.txt"
INPUT_FILE = "Inputs/day10_example.txt"
my_map = Map(INPUT_FILE)
my_map.print_trailhead_list()
# print(map.process_trailhead([0, 2]))
my_map.process_all_trailheads()
