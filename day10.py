import pandas as pd

# Can only move up, down, left, right
# trailhead starts at 0 and scored by however many 9s you can reaach from it


class Map():
    def __init__(self, file):
        with open(file, 'r') as file:
            matrix = []
            for line in file:
                matrix.append(list(line)[:-1])
        self.map = pd.DataFrame(data=matrix)
        self.print_map()
        self.peaks = self.find_peaks()

    def print_map(self):
        print("Printing map...")
        print(self.map)

    def find_peaks(self):
        peak_map = self.map.copy()
        list_of_peaks = []
        for col in peak_map.columns.to_list():
            for ix in peak_map[peak_map[col] == "9"].index.to_list():
                list_of_peaks.append([int(ix), int(col)])
        print("Found the following peaks:")
        for peak in list_of_peaks:
            peak_map.loc[peak[0], peak[1]] = "X"
        print(peak_map)
        return list_of_peaks

    def print_peak_list(self):
        print("List of peaks are:")
        for ix, peak in enumerate(self.peaks):
            print("{} - {}".format(ix, peak))

    def process_peak(self, peak):
        map = self.map.copy()
        # Get current position
        current_point = peak
        current_value = int(map.iat[current_point[0], current_point[1]])
        print(current_point, current_value)
        if current_value != 9:
            print("Peak does not end at 9, starts at", current_value)
            return 0
        bounds = self.check_bounds(current_point)
        print('bounds', bounds)
        # Find next number
        if bounds["up"]:
            up_num = int(map.iat[current_point[0] - 1, current_point[1]])
            print("Up in bounds and value is {}".format(up_num))
            if up_num == current_value - 1:
                print("Up decreases")
        if bounds["down"]:
            down_num = int(map.iat[current_point[0] + 1, current_point[1]])
            print("Down in bounds and value is {}".format(down_num))
            if down_num == current_value - 1:
                print("Down decreases")
        if bounds["left"]:
            left_num = int(map.iat[current_point[0], current_point[1] - 1])
            print("Left in bounds and value is {}".format(left_num))
            if left_num == current_value - 1:
                print("Left decreases")
        if bounds["right"]:
            right_num = int(map.iat[current_point[0], current_point[1] + 1])
            print("Right in bounds and value is {}".format(right_num))
            if right_num == current_value - 1:
                print("Right decreases")
        # Complete loop and note if there's another route
        # Stop if hit 9 or can't find next number

    def check_bounds(self, point):
        nrows, ncols = self.map.shape
        move_up = True
        move_down = True
        move_left = True
        move_right = True
        if point[0] == 0:
            move_up = False
        if point[0] == nrows:
            move_down = False
        if point[1] == 0:
            move_left = False
        if point[1] == ncols:
            move_right = False
        return {"left": move_left, "right": move_right,
                "up": move_up, "down": move_down}


# file = "Inputs/day10_input.txt"
file = "Inputs/day10_example.txt"
map = Map(file)
map.print_peak_list()
map.process_peak([0, 1])
