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
    df_temp = row.dropna().transpose().to_frame("Readings")
    df_temp["diff"] = df_temp.diff()

    if readings_safe(df_temp):
        safe_count = safe_count + 1

    else:
        print("\n\nReading unsafe, checking for removal")
        print(df_temp)

        for sub_ix, sub_row in df_temp.iterrows():
            new_test_df = df_temp.drop(index=sub_ix)
            new_test_df["diff"] = new_test_df["Readings"].diff()
            if readings_safe(new_test_df):
                damp_safe_count = damp_safe_count + 1
                print("Made safe popping out index {}".format(sub_ix))
                break

print("\nThere were:\nSafe Readings: {}\nDamped Safe Readings: {}\nTotal Safe Readings: {}".format(
    safe_count, damp_safe_count, safe_count + damp_safe_count))
