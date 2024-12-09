file = "day3_input.txt"
# file = "day3_example.txt"
with open(file, "r") as f: mem = f.read()

def eval_mul_command(memory_to_eval):
    # This function evaluates the mul command
    if ("(" not in memory_to_eval) or (")" not in memory_to_eval):
        # print("parens not in {}".format(max_memory))
        return 0

    to_eval = memory_to_eval.split(")")[0].split("(")[1].split(",")
    if to_eval[0].isnumeric() and to_eval[1].isnumeric():
        product = int(to_eval[0]) * int(to_eval[1])
        return product
    else:
        return 0



sum = 0
mul_count = 0
enable_mul = None

for index, char in enumerate(mem):
    #          012345678901
    # Look for mem(123,123)
    # or       do()
    # or       don't()
    mul_start_text = "mul("
    do_cmd_text = "do()"
    dont_cmd_text = "don't()"
    string_to_eval = mem[index : index + 7]

    product = 0

    # Chec for do()
    if string_to_eval[:4] == do_cmd_text:
        enable_mul = True
        continue

    if string_to_eval == dont_cmd_text:
        enable_mul = False
        continue

    # Check if mul command
    if string_to_eval[:4] == mul_start_text:
        max_memory = mem[index : index + 12]
        product = eval_mul_command(max_memory)
        if (product > 0):
            if (enable_mul == True) or (enable_mul == None):
                sum += product
                mul_count += 1

print("\nRunning Total = {}\nMuls {}".format(sum, mul_count))
