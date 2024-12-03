import re

def mul(a, b):
    return a * b

class Solver:

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            self.data = f.read()

    def _evaluate(self, expression):
        regex = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
        return sum(eval(x) for x in regex.findall(expression))

    def solve_first_part(self):
        return self._evaluate(self.data)
    
    def solve_second_part(self):
        slices_to_evaluate = []
        todo = True
        current_index = 0
        do_indexes = re.finditer(r"(do\(\))", self.data)
        dont_indexes = re.finditer(r"(don't\(\))", self.data)
        while True:
            if todo:
                next_dont = next(dont_indexes, None)
                if next_dont:
                    if next_dont.start() < current_index:
                        continue
                    slices_to_evaluate.append(self.data[current_index:next_dont.start()])
                    current_index = next_dont.end()
                    todo = False
                else:
                    slices_to_evaluate.append(self.data[current_index:])
                    break
            else:
                next_do = next(do_indexes, None)
                if next_do:
                    if next_do.start() < current_index:
                        continue
                    current_index = next_do.end()
                    todo = True
                else:
                    break
        return self._evaluate(''.join(slices_to_evaluate))


solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')