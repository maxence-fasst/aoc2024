import re
from collections import defaultdict

class Solver:

    def __init__(self, *args, **kwargs):
        data = []
        with open('input.txt') as f:
            for line in f.readlines():
                data.extend([int(match) for match in re.findall(r'\d+', line)])
        self.A, self.B, self.C, *self.program = data
    
    def _get_combo_operand(self, operand):
        if operand in range(4):
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        return None

    def _run_program(self):
        operation_index = 0
        while operation_index < len(self.program):
            operation, literal_operand = self.program[operation_index], self.program[operation_index + 1]
            combo_operand = self._get_combo_operand(literal_operand)
            if operation == 0: # adv
                self.A = self.A // (2**combo_operand)
            elif operation == 1: # bxl
                self.B = self.B ^ literal_operand
            elif operation == 2: # bst
                self.B = combo_operand % 8
            elif operation == 3: #jnz
                if self.A != 0:
                    operation_index = literal_operand
                    continue
            elif operation == 4: # bxc
                self.B = self.B ^ self.C
            elif operation == 5: # out
                yield f'{combo_operand % 8}'
            elif operation == 6: # bdv
                self.B = self.A // (2**combo_operand)
            elif operation == 7: # cdv
                self.C = self.A // (2**combo_operand)
            operation_index += 2

    def solve_first_part(self):
        return ','.join(list(self._run_program()))

    def solve_second_part(self):
        pass
        
                
solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')