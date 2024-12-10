import time
# record start time
start = time.time()

file = "day5_input.txt"

rules = []
pages = []

with open(file, "r") as f:
    isrules = True
    for line in f:
        # When you hit the blank line, skip it and now reading pages
        if line == "\n":
            isrules = False
            continue
        if isrules:
            rules.append(line.strip().split("|"))
        else:
            pages.append(line.rstrip().split(","))            
# Rules and Pages processed, now assess


def check_order_func(page_evaluated, rules):
    # This function returns True if in order, False if out of order
    for rule in rules:
        first_rule, second_rule = rule

        # Check if both pages in rule exist in current page
        if (first_rule in page_evaluated) and (second_rule in page_evaluated):
            # Both exist, now check order
            first_rule_index = page_evaluated.index(first_rule)
            second_rule_index = page_evaluated.index(second_rule)

            # if in order, move to the next rule
            if first_rule_index < second_rule_index:
                continue
            else:
                return False
        else:
            # Both pages must exists, skip
            continue
    # If here, then is in order
    return True



def re_order_func(page_evaluated, rules):
    # This function returns re-ordered list
    for rule in rules:
        first_rule, second_rule = rule

        # Check if both pages in rule exist in current page
        if (first_rule in page_evaluated) and (second_rule in page_evaluated):
            # Both exist, now check order
            first_rule_index = page_evaluated.index(first_rule)
            second_rule_index = page_evaluated.index(second_rule)

            # if in order, move to the next rule
            if first_rule_index < second_rule_index:
                # print("Page {} comes before {} per rule".format(first_rule, second_rule))
                continue
            else:
                # Add logic to move
                page_evaluated.insert(second_rule_index, 
                                      page_evaluated.pop(first_rule_index))
        else:
            # Both pages must exists, skip
            continue
    return page_evaluated



pages_in_order = []
middle_items = []
pages_out_of_order = []

# Evaluate Pages
for page_evaluated in pages:
    if check_order_func(page_evaluated, rules):
        pages_in_order.append(page_evaluated)
        # Add middle item to list
        middle_ix = int((len(page_evaluated) - 1)/2)
        middle_items.append(int(page_evaluated[middle_ix]))
    else:
        pages_out_of_order.append(page_evaluated)


# Part 1 Solution
end = time.time()
print("\n\nSum of middle items is {}".format(sum(middle_items)))
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

# #############################################################################################
# Part 2
# #############################################################################################

part2_middle_items = []

# Loop through pages out of order
for page_evaluated in pages_out_of_order:
    temp_list = re_order_func(page_evaluated, rules)

    num_of_attempts = 5 
    while num_of_attempts > 0:
        if check_order_func(temp_list, rules):
            middle_ix = int((len(temp_list) - 1)/2)
            part2_middle_items.append(int(temp_list[middle_ix]))
            break
        else:
            temp_list = re_order_func(temp_list, rules)
        num_of_attempts -= 1


end = time.time()
print("\n\nNew sum of middle items is {}".format(sum(part2_middle_items)))
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")


