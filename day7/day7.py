import re
from itertools import cycle, product
from operator import add, mul


class Solver:
    OPERATORS = {
        '+': add,
        '*': mul
    }

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            self.data = [[int(match) for match in re.findall(r'\d+', line)] for line in f.readlines()]

    def _generate_combinations(self, operators, length):
        return [''.join(combination) for combination in product(operators, repeat=length)]

    def _is_operation_valid(self, operation, OPERATORS):
        result, *numbers = operation
        nb_operators = len(numbers) - 1
        for combination in self._generate_combinations(OPERATORS.keys(), nb_operators):
            operation_numbers = numbers.copy()
            operators = cycle(combination)
            current_result = operation_numbers.pop(0)
            while operation_numbers:
                operator = next(operators)
                current_result = OPERATORS[operator](current_result, operation_numbers.pop(0))
                if current_result > result:
                    break
            if current_result == result:
                return True
        return False
            
    def solve_first_part(self):
        return sum(operation[0] for operation in self.data if self._is_operation_valid(operation, self.OPERATORS))
    
    def solve_second_part(self):
        new_operators = { **self.OPERATORS, '|': lambda x, y: int(f'{x}{y}') }
        return sum(operation[0] for operation in self.data if self._is_operation_valid(operation, new_operators))
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')