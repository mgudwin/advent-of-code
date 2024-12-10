import pandas as pd
import time
# record start time
start = time.time()

file = "day6_input.txt"
with open(file, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(line)[:-1])

df = pd.DataFrame(data=matrix)

print(df)

for col in df.columns.to_list():
    try:
        ix = df.index[df[col].isin(["^", ">", "<", "V"])].values[0]
        start = [ix, col]
        print("START",start)
        print(df[ix,col])
    except:
        continue
