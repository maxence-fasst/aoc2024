import re
from operator import mul


class Solver:
    REGEX_MUL = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            self.data = f.read()

    def solve_first_part(self):
        return sum(eval(x) for x in self.REGEX_MUL.findall(self.data))
    
    def solve_second_part(self):
        do_indexes = [find.start() for find in re.finditer(r"(do\(\))", self.data)]
        dont_indexes = [find.start() for find in re.finditer(r"(don't\(\))", self.data)]
        mul_indexes = { find.start(): find.group() for find in self.REGEX_MUL.finditer(self.data) }
        todo = True
        result = 0
        for index in sorted([*do_indexes, *dont_indexes, *mul_indexes.keys()]):
            if index in do_indexes:
                todo = True
            elif index in dont_indexes:
                todo = False
            elif index in mul_indexes.keys():
                if todo:
                    result += eval(mul_indexes[index])
        return result
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')