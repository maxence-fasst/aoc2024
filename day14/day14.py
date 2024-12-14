import re
from collections import defaultdict

class Solver:

    def __init__(self, *args, **kwargs):
        self.len_x = 101
        self.len_y = 103
        self.robots = []
        with open('input.txt') as f:
            for line in f.readlines():
                self.robots.append([int(match) for match in re.findall(r'-?\d+', line)])

    def _get_target_position(self, start_x, start_y, v_x, v_y, nb_steps):
        return (start_x + v_x * nb_steps) % self.len_x, (start_y + v_y * nb_steps) % self.len_y
                
    def solve_first_part(self):
        positions = [self._get_target_position(*robot, 100) for robot in self.robots]
        quarters = [
            [(0, self.len_x // 2), (0, self.len_y // 2)], 
            [(self.len_x // 2 + 1, self.len_x), (0, self.len_y // 2)], 
            [(0, self.len_x // 2), (self.len_y // 2 + 1, self.len_y)], 
            [(self.len_x // 2 + 1, self.len_x), (self.len_y // 2 + 1, self.len_y)]
        ]
        result = 1
        for limit_x, limit_y in quarters:
            result *= sum(x in range(*limit_x) and y in range(*limit_y) for x, y in positions)
        return result
    
    def _is_tree(self, positions):
        nb_x  = defaultdict(int)
        for x in range(self.len_x):
            trunk = ' ' * self.len_y
            for y in range(self.len_y):
                if (x, y) in positions:
                    trunk = trunk[:y] + '#' + trunk[y+1:]
            nb_x[x] = max([len(match) for match in re.findall(r'#+', trunk)] or [0])
            if max([len(match) for match in re.findall(r'#+', trunk)] or [0]) >= 30: # arbitrary value
                return True 
        return False

    def solve_second_part(self):
        seconds = 0
        while True:
            positions = [self._get_target_position(*robot, seconds) for robot in self.robots]
            if self._is_tree(positions):
                return seconds
            seconds += 1
        
                
solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')