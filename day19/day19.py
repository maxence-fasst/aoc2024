from collections import deque

class Solver:

    def __init__(self, *args, **kwargs):
        self.designs = []
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                if ',' in line:
                    self.towels = line.replace(' ', '').split(',')
                else:
                    self.designs.append(line)
                    
    def _get_nb_possible_result(self, design):
        queue = deque([0])  
        visited = set()
        while queue:
            current_index = queue.popleft()
            if current_index == len(design):
                return True
            if current_index in visited:
                continue
            visited.add(current_index)
            for towel in self.towels:
                if design.startswith(towel, current_index):
                    queue.append(current_index + len(towel))
        return False

    def solve_first_part(self):
        return sum([self._get_nb_possible_result(design) > 0 for design in self.designs])
        
    def solve_second_part(self):
        pass

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')