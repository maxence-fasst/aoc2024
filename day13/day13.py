import re
import numpy as np

class Solver:

    def __init__(self, *args, **kwargs):
        self.equations = []
        with open('input.txt') as f:
            equation = []
            for line in f.readlines():
                line = line.replace('\n', '')
                if not line:
                    self.equations.append(equation)
                    equation = []
                    continue
                equation.append([int(match) for match in re.findall(r'\d+', line)])
            self.equations.append(equation)

    def _solve_equation(self, eq1, eq2, results, offset=0):
        A1, B1 = eq1
        A2, B2 = eq2
        result1, result2 = [r + offset for r in results]
        eq_array = np.array([[A1, A2], [B1, B2]], np.int64)
        eq_results = np.array([[result1], [result2]], np.int64)
        solution = np.linalg.solve(eq_array, eq_results)
        press_a, press_b = round(solution[0][0]), round(solution[1][0])
        # round and test if the solution is correct
        if round(press_a) * A1 + round(press_b) * A2 == result1 and round(press_a) * B1 + round(press_b) * B2 == result2:
            return round(press_a * 3 + press_b)
        return 0
                
    def solve_first_part(self):
        return sum(self._solve_equation(*equation) for equation in self.equations)
    
    def solve_second_part(self):
        return sum(self._solve_equation(*equation, offset=10_000_000_000_000) for equation in self.equations)
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')
