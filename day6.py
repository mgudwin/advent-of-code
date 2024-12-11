import pandas as pd
import time
# record start time
start = time.time()

file = "Inputs/day6_input.txt"
with open(file, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(line)[:-1])

df = pd.DataFrame(data=matrix)

r, c = None, None
direction = None

# Find the start
for col in df.columns.to_list():
    try:
        ix = df.index[df[col].isin(["^", ">", "<", "V"])].values[0]
        r, c = ix, col
        direction = df.loc[r, c]
        break
    except:
        continue
start_pos = [r, c]

# Move, up/left and down/right are the same since I
# pass a series (row/col depending on dir)
def move(direction, start, series, end):
    # only need to pass series to determine how far to move
    if direction == '^' or direction == "<":
        ix = start[0]
        barrier = False
        while (ix in range(series.shape[0])) and (barrier != "#"):
            barrier = series[ix - 1]
            ix -= 1
            if ix == 0 or ix == (len(series) - 1):
                end = True
        return ix + 1, end

    if direction == ">" or direction == "V":
        ix = start[1]
        barrier = False
        while (ix in range(series.shape[0])) and (barrier != "#"):
            barrier = series[ix + 1]
            ix -= 1
            if ix == 0 or ix == (len(series) - 1):
                end = True
        return ix + 1, end


end = False
positions = [[r, c, direction]]

while not end:
    if direction == "^" and not end:
        r, end = move("^", [r,c], df[c], end)
        direction = ">"
        positions.append([r, c, direction])
    if direction == ">" and not end:
        c, end = move(">", [r,c], df[r], end)
        positions.append([r, c, direction])
        direction = "V"
    if direction == "V" and not end:
        r, end = move("V", [r,c], df[c], end)
        positions.append([r, c, direction])
        direction = "<"
    if direction == "<" and not end:
        c, end = move("<", [r,c], df[r], end)
        positions.append([r, c, direction])
        direction = "^"
 
locations = [start_pos]
for pos in positions:
    c2 = pos[1]
    r2 = pos[0]
    c1 = locations[-1][1]
    r1 = locations[-1][0]

    if c2 > c1:
        for c in range(c2 - c1):
            locations.append([r2, c2 - c])
    if c1 > c2:
        for c in range(c1 - c2):
            locations.append([r2, c1 - c])
#
    if r2 > r1:
        for r in range(r2 - r1):
            locations.append([r2 - r, c2])
    if r1 > r2:
        for r in range(r1 - r2):
            locations.append([r1 - r, c2])
loc_df = pd.DataFrame(locations).drop_duplicates()
print(loc_df)
print(loc_df.shape)
# print(locations)

