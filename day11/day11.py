import re
from collections import defaultdict

class Solver:

    def __init__(self, *args, **kwargs):
        self.data = defaultdict(int)
        with open('input.txt') as f:
            rocks = [int(match) for match in re.findall(r'\d+', f.read())]
        for rock in rocks:
            self.data[rock] += 1

    def _get_new_values(self, rock):
        if rock == 0:
            return 1,
        str_rock = str(rock)
        if len(str_rock) % 2 == 0:
            return int(str_rock[:len(str_rock) // 2]), int(str_rock[len(str_rock) // 2:])
        return (rock * 2024),

    def _blink(self, nb_cycles):
        data_copy = self.data.copy()
        for _ in range(nb_cycles):
            new_dict = defaultdict(int)
            for rock, nb in data_copy.items():
                for new_value in self._get_new_values(rock):
                    new_dict[new_value] += nb
            data_copy = new_dict
        return sum(data_copy.values())
        
    def solve_first_part(self):
        return self._blink(25)
    
    def solve_second_part(self):
        return self._blink(75)
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')