from functools import cache
from itertools import product

class Solver:

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            self.numbers = [int(line.strip()) for line in f.readlines()] 

    @cache
    def  _run(self, number, nb_cycles = 2000):
        for i in range(nb_cycles):
            # step 1
            number = (number ^ (number * 64)) % 16777216
            # step 2
            number = (number ^ (number // 32)) % 16777216
            # step 3
            number = (number ^ (number * 2048)) % 16777216
        return number
        
    def solve_first_part(self):
        return sum(self._run(number) for number in self.numbers)
        
    def solve_second_part(self):
       pass

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')