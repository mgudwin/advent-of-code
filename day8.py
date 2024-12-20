import pandas as pd
import numpy as np

# ###########################################################
# Inputs
# ###########################################################
file = "Inputs/day8_example.txt"

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

def calculate_antinodes(antenna_locations, df):
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
                try:
                    if df.loc[anode1[0], anode1[1]] == ".":
                        # df.loc[anode1[0], anode1[1]] = key + "AN"
                        if key in antinote_location:
                            antinote_location[key].append(anode1)
                        else:
                            antinote_location[key] = [anode1]
                except:
                    # print("{} out of bounds".format(anode1))
                    continue
                try:
                    if df.loc[anode2[0], anode2[1]] == ".":
                        # df.loc[anode2[0], anode2[1]] = key + "AN"
                        if key in antinote_location:
                            antinote_location[key].append(anode2)
                        else:
                            antinote_location[key] = [anode2]
                except:
                    # print("{} out of bounds".format(anode2))
                    continue
    return antinote_location


antenna_locations = assemble_list_of_antenna(df)
node_locations = calculate_antinodes(antenna_locations, df)

# ###########################################################
# Post Process
# ###########################################################

final_array = []
for key in node_locations:
    # print("{} has {} locations".format(key, len(np.unique(node_locations[key]))))
    for location in np.unique(node_locations[key]):
        print("{} : {}".format(key, location))
        # final_array.append(location)

# print("There are {} locations total".format(len(final_array)))
# print("There are {} totally unique locations".format(len(np.unique(final_array))))
print("Done")