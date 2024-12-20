import copy
import time
start = time.time()


class TestClass:
    def __init__(self):
        self.solution = None
        self.terms = None
        self.operators = None
        self.base = 3
        self.results = []
    
    def produce_operators(self):
        num_terms = len(self.terms)
        operator_list = []
        if self.base == 2:
            for i in range(2**(num_terms - 1)):
                operator_list.append(
                    list(format(i, f'0{num_terms - 1}b').replace(
                        "0", "+").replace(
                            "1", "*"
                        )
                    )
                )
        elif self.base == 3:
            for i in range(3**(num_terms - 1)):
                operator_list.append(
                    list(str(self.convertToTernary(i)[1 - num_terms:]
                             ).rjust(num_terms - 1, '0').replace(
                                 "0", "+").replace(
                                     "1", "*").replace(
                                         "2", "|"
                                     )
                                 )
                            )
        return operator_list
    

    def eval_operations(self):
        result = False
        for operator_group in self.operators:
            terms = copy.deepcopy(self.terms)
            running_total = int(terms.pop(0))
            for ix in range(len(terms)):
                if operator_group[ix] == "+":
                    running_total = int(running_total) + int(terms.pop(0))
                elif operator_group[ix] == "*":
                    running_total = int(running_total) * int(terms.pop(0))
                elif operator_group[ix] == "|":
                    running_total = str(running_total) + str(terms.pop(0))
            if str(running_total) == str(self.solution):
                result = True
                break
        return [self.solution, result, running_total]


    def read_value(self, line):
        self.solution = line[0]
        self.terms = line[1]
        self.operators = self.produce_operators()
        self.results.append(self.eval_operations())


    def convertToTernary(self, N):
        if N == 0:
            return '0'
        elif N == 1:
            return '1'
        else:
            return self.convertToTernary(N // 3) + str(N % 3)
    


# file = "Inputs/day7_example.txt"
file = "Inputs/day7_input.txt"


t = TestClass()
with open(file, 'r') as file:
    test_vals = []
    correct_vals = []
    for line in file:
        solution, coeffs = line.rstrip().split(":")
        coeffs = coeffs.lstrip().split(" ")
        t.read_value([solution, coeffs])

print("Done")
sum = 0
for test in t.results:
    solution = int(test[0])
    correct = test[1]
    math = int(test[2])
    if correct:
        sum += solution

print("Sum is {}".format(sum))


end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

