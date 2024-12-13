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

start_direction = direction
start_position = current_pos


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
print("Part 1 completes in",
      (end-start) * 10**3, "ms")

# Part 2
# p1 = r1,c1
# p2 = (r1+1),c2
# p3 = (r4-1),c3
# p4 = (r1-1),(c1-1)
# if O is one of these and the path crosses in it,
# or O makes the path cross into it, that will
# cause a loop

# For each position, add barrier and check if loop
# if loop if last x positions are repeats
# if loop, add position to new list
start = time.time()
loop_positions = []
for enums, position in enumerate(positions[1:]):
    turn_list = []
    temp_df = df.copy()
    temp_df.iloc[position[0], position[1]] = "#"
    current_pos = start_position
    direction = start_direction

    end = False
    _positions = [current_pos]
    while check_in_bounds(current_pos, direction) and not end:
        r, c = current_pos

        # Check for loop
        if len(turn_list) >= 10:
            last_4_turns = "".join(str(t) for t in  turn_list[-4:])
            all_turns = "".join(str(t) for t in  turn_list)
            if all_turns.count(last_4_turns) >= 2:
                # In a loop, break
                loop_positions.append(position)
                break

        if direction == "^":
            while (r >= 0):
                if r == 0:
                    end = True
                    break
                next_step = temp_df.loc[r-1, c] != "#"
                if next_step:
                    r -= 1
                    current_pos = [r, c]
                    _positions.append(current_pos)
                else:
                    direction = change_dir(direction)
                    turn_list.append(current_pos)
                    break

        elif direction == ">":
            while (c <= ncols - 1):
                if c == ncols - 1:
                    end = True
                    break
                next_step = temp_df.loc[r, c+1] != "#"
                if next_step:
                    c += 1
                    current_pos = [r, c]
                    _positions.append(current_pos)
                else:
                    direction = change_dir(direction)
                    turn_list.append(current_pos)
                    break

        elif direction == "V":
            while (r <= nrows - 1):
                if r == nrows - 1:
                    end = True
                    break
                next_step = temp_df.loc[r+1, c] != "#"
                if next_step:
                    r += 1
                    current_pos = [r, c]
                    _positions.append(current_pos)
                else:
                    direction = change_dir(direction)
                    turn_list.append(current_pos)
                    break


        elif direction == "<":
            while (c >= 0):
                if c == 0:
                    end = True
                    break
                next_step = temp_df.loc[r, c-1] != "#"
                if next_step:
                    c -= 1
                    current_pos = [r, c]
                    _positions.append(current_pos)
                else:
                    direction = change_dir(direction)
                    turn_list.append(current_pos)
                    break

# print("Part 2 done, loop positions are at:\n{}".format(loop_positions))
loop_df = pd.DataFrame(loop_positions)
print("Loop df shape is ", loop_df.shape)
print("Loop df drop dupes", loop_df.drop_duplicates().shape)
print("There are {} positions which will cause loops".format(len(loop_positions)))
end = time.time()
print("Part 2 takes:",
      (end-start) * 10**3, "ms")