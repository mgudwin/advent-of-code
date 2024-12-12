import pandas as pd
import time
# record start time
start = time.time()

# file = "Inputs/day6_example.txt"
file = "Inputs/day6_input.txt"
with open(file, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(line))

df = pd.DataFrame(data=matrix)
df = df.iloc[:,:-1]

nrows, ncols = df.shape
r, c = None, None
direction = None

# Find the start
for ix, row in df.iterrows():
    for col, r in enumerate(row):
        if r in ["^", ">", "<", "V"]:
            current_pos = [ix, col]
            direction = r


def check_in_bounds(current_pos, direction):
    r, c = current_pos
    if r == 0 and direction == '^':
        return False
    elif r == nrows and direction == 'V':
        return False
    elif c == 0 and direction == '<':
        return False
    elif c == ncols and direction == '>':
        return False
    else:
        return True

def change_dir(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'V'
    elif direction == 'V':
        return '<'
    elif direction == '<':
        return '^'
    else:
        return 0

end = False
positions = [current_pos]
while check_in_bounds(current_pos, direction) and not end:
    r, c = current_pos

    if direction == "^":
        while (r >= 0):
            if r == 0:
                end = True
                break
            next_step = df.loc[r-1, c] != "#"
            if next_step:
                r -= 1
                current_pos = [r, c]
                positions.append(current_pos)
            else:
                direction = change_dir(direction)
                break

    elif direction == ">":
        while (c <= ncols - 1):
            if c == ncols - 1:
                end = True
                break
            next_step = df.loc[r, c+1] != "#"
            if next_step:
                c += 1
                current_pos = [r, c]
                positions.append(current_pos)
            else:
                direction = change_dir(direction)
                break

    elif direction == "V":
        while (r <= nrows - 1):
            if r == nrows - 1:
                end = True
                break
            next_step = df.loc[r+1, c] != "#"
            if next_step:
                r += 1
                current_pos = [r, c]
                positions.append(current_pos)
            else:
                direction = change_dir(direction)
                break


    elif direction == "<":
        while (c >= 0):
            if c == 0:
                end = True
                break
            next_step = df.loc[r, c-1] != "#"
            if next_step:
                c -= 1
                current_pos = [r, c]
                positions.append(current_pos)
            else:
                direction = change_dir(direction)
                break


print("Done")
print("There are {} unique positions".format(pd.DataFrame(positions).drop_duplicates().shape[0]))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
