import pandas as pd

# Part 1
df = pd.read_csv("day1_input.txt", sep="   "
                 , engine="python"
                 , header=None
                 , names=["list1", "list2"])
list1 = df[["list1"]].sort_values("list1").reset_index(drop=True)
list2 = df[["list2"]].sort_values("list2").reset_index(drop=True)

df_lists = pd.concat([list1, list2], axis=1).reset_index()
df_lists["diff"] = df_lists["list1"] - df_lists["list2"]
df_lists["diff"] = df_lists["diff"].abs()

print (df_lists["diff"].sum())

# Part 2
running_sum = 0
for ix, row in list1.iterrows():
    value = row.values[0]
    occurrences = list2.loc[list2.list2 == value].shape[0]
    running_sum = running_sum + (value*occurrences)

print(running_sum)