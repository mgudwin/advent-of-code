from collections import deque

# from typing import List
from copy import deepcopy

from tabulate import tabulate

# from types import CapsuleType


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
        self.known_trails = []

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
        visited = [trailhead_loc]
        queue.append(trailhead_loc)
        nines = []
        while queue:
            path = []
            curr_point = queue.popleft()
            curr_value = self.map[curr_point[0]][curr_point[1]]
            path.append(f"{curr_point}-{curr_value}")
            for neighbor in self.get_neighbors(curr_point):
                neighbor_value = self.map[neighbor[0]][neighbor[1]]
                if neighbor_value == curr_value + 1:
                    path.append(f"{neighbor}-{neighbor_value}")
                    if neighbor_value == 9:
                        nines.append(str(neighbor))
                    if str(neighbor) not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        nines = list(set(nines))
        return nines

    def trailhead_dfs(self, node: tuple, visited: list, end: int, path: list):
        """This is a dfs implementation"""
        node_value = self.map[node[0]][node[1]]
        visited.append(node)
        path.append(node)
        if node_value == end:
            path_str = ",".join([f"({p[0]}-{p[1]})" for p in path])
            self.known_trails.append(path_str)
            path = []
            return path
        neighbors = self.get_neighbors(node)
        if len(neighbors) == 0:
            path.remove(node)
            return path
        for neighbor in self.get_neighbors(node):
            neighbor_value = self.map[neighbor[0]][neighbor[1]]
            if neighbor_value == node_value + 1:
                self.trailhead_dfs(neighbor, visited, end, path)

    def get_neighbors(self, current_point):
        """Function to get neighbors for point"""
        neighbors = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for direction in directions:
            c = [current_point[0] + direction[0], current_point[1] + direction[1]]
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
            new_peaks = self.process_trailhead(trailhead)
            _score = len(new_peaks)
            peaks += new_peaks
            score += _score
        print(f"Total score is {score}")

    def process_all_trailheads_dfs(self):
        """Function to process all trailheads on map"""
        for trailhead in self.trailheads:
            self.trailhead_dfs(node=trailhead, visited=[], end=9, path=[])
        self.known_trails = list(set(self.known_trails))
        print(f"Total number of trails are {len(self.known_trails)}")


INPUT_FILE = "Inputs/day10_input.txt"
# INPUT_FILE = "Inputs/day10_example.txt"
my_map = Map(INPUT_FILE)
# my_map.print_trailhead_list()
my_map.process_all_trailheads_dfs()
# my_map.process_all_trailheads()
