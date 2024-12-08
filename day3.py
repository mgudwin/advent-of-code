file = "day3_input.txt"
# file = "day3_example.txt"
with open(file, "r") as f: mem = f.read()

sum = 0
starts_with_mul = 0

for index, char in enumerate(mem):
    #          012345678901
    # Look for mem(123,123)
    search_term = "mul("
    string_to_eval = mem[index : index+4]

    product = 0

    if string_to_eval == search_term:
        max_memory = mem[index : index + 12]
        to_eval = max_memory.split(")")[0].split("(")[1].split(",")
        if to_eval[0].isnumeric() and to_eval[1].isnumeric():
            product = int(to_eval[0]) * int(to_eval[1])
            eval_text = "product is " + str(product)
            sum += product
        else:
            eval_text = "<--- This is invalid"
        print("ix: {}\tMax Mem to Eval '{}'\t{}".format(index
                                                             , max_memory
                                                             , eval_text))

print("\nRunning Total = {}".format(sum))
