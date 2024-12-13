# For each test value
class Test:
    def __init__(self):
        self.solution = None
        self.terms = None
        self.operator_count = None
        self.operators = None
        self.results = []

    def permutations(self):
        permutation_list = []
        for i in range(self.operator_count):
            operator_list = list(format(i,f'0{self.operator_count - 1}b').
                        replace("0", "+").replace("1", "*"))
            permutation_list.append(operator_list)
        return permutation_list
    
    def evaluate_permutations(self):
        result = False
        for operator_group in self.operators:
            temp = eval(self.terms[0] + str(operator_group[0]) + str(self.terms[1]))
            for i in range(1, self.operator_count - 1):
                temp = eval(str(temp) + str(operator_group[i] + str(self.terms[i + 1])))
            if temp == int(self.solution):
                result = True
        return [self.solution, result]

    def process_values(self, test_value):
        self.solution = test_value[0]
        self.terms = test_value[1]
        self.operator_count = len(self.terms)
        self.operators = self.permutations()
        self.results.append(self.evaluate_permutations())

 
# file = "Inputs/day7_example.txt"
file = "Inputs/day7_input.txt"

t = Test()
with open(file, 'r') as file:
    test_vals = []
    correct_vals = []
    for line in file:
        solution, coeffs = line.rstrip().split(":")
        coeffs = coeffs.lstrip().split(" ")
        t.process_values([solution, coeffs])

sum = 0
for results in t.results:
    if results[1]:
        sum += int(results[0])

print(sum)
print("Done")