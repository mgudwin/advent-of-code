import pandas as pd

file = "day4_input.txt"

with open(file, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(line)[:-1])

df = pd.DataFrame(data=matrix)

# ###############################################################################
# Part 1
# ###############################################################################

xmas_count = 0
x_mas_count = 0

# Count instances in each column
for col in df.columns.to_list():
    text = "".join(df[col].to_list())
    xmas_count += text.count("XMAS")
    xmas_count += text.count("SAMX")

# Count instances in each row
for ix, row in df.iterrows():
    text = "".join(row.to_list())
    xmas_count += text.count("XMAS")
    xmas_count += text.count("SAMX")

# Count diagonal instances in each 4x4 subframe
ncols, nrows = df.shape
for x in range(ncols - 3):
    for y in range(nrows - 3):
        # Get 4x4 subframe to evaluate
        subframe = df.loc[x: x + 3,
                          y: y + 3].copy().reset_index(drop=True)

        # Checks for "XMAS"
        # Check diagonal
        text = "".join([subframe.iloc[i, i] for i in range(4)])
        if (text == "XMAS") or (text == "SAMX"):
            xmas_count += 1
        text = "".join([subframe.iloc[i, 3 - i] for i in range(4)])
        if (text == "XMAS") or (text == "SAMX"):
            xmas_count += 1

print("There are {} instances of 'XMAS' in any orientation".format(xmas_count))

# ###############################################################################
# Part 2
# ###############################################################################

for x in range(ncols - 2):
    for y in range(nrows - 2):
        # Get 3x3 subframe to evaluate
        subframe = df.loc[x: x + 2,
                        y: y + 2].copy().reset_index(drop=True)

        # Checks for "MAS"
        # Check diagonal
        text1 = "".join([subframe.iloc[i, i] for i in range(3)])
        text2 = "".join([subframe.iloc[i, 2 - i] for i in range(3)])
        if ((text1 == "MAS") or (text1 == "SAM")):
            if ((text2 == "MAS") or (text2 == "SAM")):
                x_mas_count += 1

print("There are {} instances of X-'MAS' in here".format(x_mas_count))
