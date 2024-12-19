from functools import cache

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

    @cache       
    def _get_nb_possible_result(self, design, start=0):
        if start == len(design):
            return 1
        result = 0
        for towel in self.towels:
            if design.startswith(towel, start):
                result += self._get_nb_possible_result(design, start=start + len(towel))
        return result

    def solve_first_part(self):
        return sum([self._get_nb_possible_result(design) > 0 for design in self.designs])
        
    def solve_second_part(self):
        return sum([self._get_nb_possible_result(design) for design in self.designs])

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')