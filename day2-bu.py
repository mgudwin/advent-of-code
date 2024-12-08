import pandas as pd
from tabulate import tabulate

in_df = pd.read_csv("day2_input.txt"
# in_df = pd.read_csv("day2_example.txt"
                    , sep=" "
                    , header=None)

print("INPUT DATA")
print(in_df)

safe_count = 0
damp_safe_count = 0

def readings_safe(df):
    # get diffs into list
    l = df["diff"].dropna().to_list()
    # Perform checks
    # All dec/inc?
    inc_dec = all( x <= 0 for x in l ) or all( x >= 0 for x in l )
    # Count of too much change
    bad_change = any( ( abs(x) > 3 ) or ( abs(x) < 1 ) for x in l )
    return inc_dec and not(bad_change)


# Cycle through each reading 
for ix, row in in_df.iterrows():
    # print("\nrow: {}".format(ix))
    # print(row)
    df_temp = row.dropna().transpose().to_frame("Readings")
    df_temp["diff"] = df_temp.diff()
    # df_temp["diff2"] = df_temp["diff"].diff()

    if readings_safe(df_temp):
        safe_count = safe_count + 1
        # print("Totally safe {}".format(safe_count))

    else:
        print("\n\nReading unsafe, checking for removal")
        print(df_temp)
        # Get counts 
        count_pos = df_temp.loc[df_temp["diff"] > 0].shape[0]
        count_neg = df_temp.loc[df_temp["diff"] < 0].shape[0]
        count_large = df_temp.loc[abs(df_temp["diff"]) > 3].shape[0]
        count_zero = df_temp.loc[df_temp["diff"] == 0].shape[0]

        # If there are more than 2 large or zero, can't fix
        if count_zero + count_large > 1:
            print("There are too many out of bounds readings")
            continue

        # If there's more than 2 that aren't the same sign, 
        if (count_pos > 2) and (count_neg > 2):
            print("There are too many +/- readings")
            continue

        # If there are more +
        if count_pos > count_neg:
        # if df_temp.loc[1, "diff"] > 0:
            # inc, remove first bad reading
            bad_reading = df_temp.index[(df_temp["diff"] > 3) | (df_temp["diff"] < 1)][0]
            temp = df_temp.drop(index=bad_reading - 1)
        else:
            # dec, remove first bad reading    
            bad_reading = df_temp.index[(df_temp["diff"] < -3) | (df_temp["diff"] > -1)][0]
            temp = df_temp.drop(index=bad_reading - 1)
        # recalc diff and retest
        print("\nRemoving index {}".format(bad_reading - 1))
        temp["diff"] = temp["Readings"].diff()
        # print('\n')
        print(temp)
        if readings_safe(temp):
            damp_safe_count = damp_safe_count + 1
            print("++++Safety Acheived! {}".format(damp_safe_count))
            # print('\n\n')
        else:
            print("----Removal did not make safe")
            # print('\n\n')

print("\nThere were:\nSafe Readings: {}\nDamped Safe Readings: {}\nTotal Safe Readings: {}".format(
    safe_count, damp_safe_count, safe_count + damp_safe_count))
