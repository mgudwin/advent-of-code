import pandas as pd
import numpy as np


class city_scape():
    def __init__(self):
        self.map = None
        self.map_dimensions = None
        self.antenna_locations = {}
        self.antinode_locations = []

    def read_map(self, file):
        with open(file, 'r') as file:
            matrix = []
            for line in file:
                matrix.append(list(line))
        self.map = pd.DataFrame(data=matrix)
        self.map.drop(self.map.columns[-1], axis=1, inplace=True)
        self.map_dimensions = self.map.shape

    def print_map(self, ant=False):
        if ant:
            temp = self.map.copy()
            for location in self.antinode_locations:
                temp.loc[location[0], location[1]] = "#"
            print(temp)
        else:
            print(self.map)

    def assemble_list_of_antenna(self):
        for r, row in self.map.iterrows():
            for c, cell in enumerate(row):
                if cell == ".":
                    continue
                else:
                    if cell in self.antenna_locations:
                        self.antenna_locations[cell].append((r, c))
                    else:
                        self.antenna_locations[cell] = [(r, c)]

    def return_antinode_group(self, p1, p2):
        vector = np.subtract(p2, p1)
        anode1 = np.subtract(p1, vector)
        anode2 = np.add(p2, vector)
        return (anode1, anode2)

    def return_all_antinodes(self, p1, p2):
        anode_list = []
        vector = np.subtract(p2, p1)
        anode1 = np.subtract(p1, vector)
        while self.check_if_in_bounds(anode1):
            anode1 = np.subtract(anode1, vector)
            if self.check_if_in_bounds(anode1):
                anode_list.append(anode1)
        anode2 = np.add(p2, vector)
        while self.check_if_in_bounds(anode2):
            anode2 = np.add(anode2, vector)
            if self.check_if_in_bounds(anode2):
                anode_list.append(anode2)
        return (anode_list)

    def check_if_in_bounds(self, anode):
        num_row, num_col = self.map_dimensions
        return (anode[0] >= 0) and (anode[0] < num_row) and\
            (anode[1] >= 0) and (anode[1] < num_col)

    def calculate_antinodes(self, max_count=2):
        for frequency in self.antenna_locations:
            num_of_antennas = len(self.antenna_locations[frequency])
            for ix in range(num_of_antennas):
                for ix2 in range(num_of_antennas):
                    if ix == ix2:
                        continue
                    p1 = self.antenna_locations[frequency][ix]
                    p2 = self.antenna_locations[frequency][ix2]
                    anode1, anode2 = self.return_antinode_group(p1, p2)
                    if self.check_if_in_bounds(anode1):
                        self.antinode_locations.append(anode1)
                    if self.check_if_in_bounds(anode2):
                        self.antinode_locations.append(anode2)
                    if max_count > 2:
                        self.antinode_locations.append(p1)
                        self.antinode_locations.append(p2)
                        for anode in self.return_all_antinodes(p1, p2):
                            if self.check_if_in_bounds(anode):
                                self.antinode_locations.append(anode)

    def calculate_distinct_nodes(self):
        print("There are {} disctinct antinode locations".format(
            len(np.unique(self.antinode_locations, axis=0))))


# ###########################################################
# Inputs
# ###########################################################
# file = "Inputs/day8_example.txt"
file = "Inputs/day8_input.txt"

city = city_scape()
city.read_map(file)
print('Printing whole map')
city.print_map(ant=False)
city.assemble_list_of_antenna()
city.calculate_antinodes(max_count=10)
print('Printing antinode locations')
city.print_map(ant=True)
city.calculate_distinct_nodes()
