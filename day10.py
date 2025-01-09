from collections import deque, defaultdict

# from typing import List
from copy import deepcopy
from tabulate import tabulate

# Can only move up, down, left, right
# trailhead starts at 0 and scored by however many 9s you can reaach from it


class Map:
    def __init__(self, file):
        with open(file, "r") as file:
            contents = file.read()
        rows = contents.strip().split("\n")
        self.map = [list(x) for x in rows]
        self.map = [[int(char) for char in row] for row in self.map]
        self.ncols = len(self.map)
        self.nrows = len(self.map[0])
        self.headers = [str(i) for i in range(self.ncols)]
        self.print_map(self.map)
        self.trailheads = self.find_trailheads()

    def print_map(self, map):
        print("Printing map...")
        print(tabulate(map, tablefmt="plain", headers=self.headers, showindex=True))

    def find_trailheads(self):
        trailhead_map = deepcopy(self.map)
        list_of_trailheads = []
        for row in range(len(trailhead_map)):
            for col in range(len(trailhead_map[0])):
                if trailhead_map[row][col] == 0:
                    list_of_trailheads.append([row, col])
        return list_of_trailheads

    def print_trailhead_list(self):
        print("List of trailheads in [row, col] format are:")
        for trailhead in self.trailheads:
            print("{}".format(trailhead))

    def process_trailhead(self, trailhead_loc: list):
        queue = deque()
        nines = []
        visited = {}
        visited[str(trailhead_loc)] = True
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
                        visited[str(neighbor)] = True
                        queue.append(neighbor)
        nines = list(set(nines))
        return nines

    def get_neighbors(self, current_point):
        neighbors = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir in directions:
            c = [current_point[0] + dir[0], current_point[1] + dir[1]]
            if self.check_bounds(c):
                neighbors.append(c)
        return neighbors

    def check_bounds(self, point):
        return (
            point[0] >= 0
            and point[1] >= 0
            and point[0] < self.nrows
            and point[1] < self.ncols
        )

    def process_all_trailheads(self):
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
        print("Total score is {}".format(score))
        # print("Here are all the peaks:\n", peaks)


file = "Inputs/day10_input.txt"
# file = "Inputs/day10_example.txt"
map = Map(file)
map.print_trailhead_list()
# print(map.process_trailhead([0, 2]))
map.process_all_trailheads()

# 298 was the first answer and was too low
