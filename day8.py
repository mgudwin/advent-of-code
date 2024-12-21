import pandas as pd
import numpy as np

# ###########################################################
# Inputs
# ###########################################################
# file = "Inputs/day8_example.txt"
file = "Inputs/day8_input.txt"

with open(file, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(line))

df = pd.DataFrame(data=matrix)
df.drop(df.columns[-1], axis=1, inplace=True)
print(df)

# ###########################################################
# Process
# ###########################################################

def calc_antinode_locations(p1, p2):
    p21 = np.subtract(p2, p1)
    p12 = np.subtract(p1, p2)
    anode1 = p1 + p12
    anode2 = p2 + p21
    return (p21, p12, anode1, anode2)

def assemble_list_of_antenna(df):
    antenna_dict = {}
    for r, row in df.iterrows():
        for c, cell in enumerate(row):
            if cell == ".":
                continue
            else:
                # check if in antenna_dict
                if cell in antenna_dict:
                    antenna_dict[cell].append((r, c))
                else:
                    antenna_dict[cell] = [(r, c)]
    return antenna_dict

def check_if_in_bounds(point, num_row, num_col):
    return (
        ((point[0] >= 0) and (point[0] <= num_col)) and 
        ((point[1] >= 0) and (point[1] <= num_row))         
        )

def calculate_antinodes(antenna_locations, df):
    num_row, num_col = df.shape
    antinote_location = {}
    for key in antenna_locations:
        length_of_points = len(antenna_locations[key])
        for ix in range(length_of_points):
            for ix2 in range(length_of_points):
                if ix == ix2:
                    continue
                p1 = antenna_locations[key][ix]
                p2 = antenna_locations[key][ix2]
                p21, p12, anode1, anode2 = calc_antinode_locations(p1, p2)
                
                if check_if_in_bounds(anode1, num_row, num_col):
                    if key in antinote_location:
                        antinote_location[key].append(anode1)
                    else:
                        antinote_location[key] = [anode1]
                if check_if_in_bounds(anode2, num_row, num_col):
                    if key in antinote_location:
                        antinote_location[key].append(anode2)
                    else:
                        antinote_location[key] = [anode2]
    return antinote_location


antenna_locations = assemble_list_of_antenna(df)
node_locations = calculate_antinodes(antenna_locations, df)

# ###########################################################
# Post Process
# ###########################################################

final_array = []

ant_str_list = []
for key in node_locations:
    for ix, location in enumerate((node_locations[key])):
        ant_str_list.append("{} : {}".format(key, "-".join(np.char.mod('%d', location))))

for ix, p in enumerate(set(ant_str_list)):
    print("{} - {}".format(ix, p))

print("Done, there are {} unique antinodes".format(len(set(ant_str_list))))

