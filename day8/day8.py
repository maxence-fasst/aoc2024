import re
from collections import defaultdict
from itertools import product


class Solver:

    def __init__(self, *args, **kwargs):
        self.grid = []
        self.nodes = defaultdict(set)
        with open('input.txt') as f:
            for i, line in enumerate(f.readlines()):
                line = line.replace('\n', '')
                self.grid.append(line)
                for match in re.finditer(r'[^\.]', line):
                    self.nodes[match.group()].add((i, match.start()))
        self.grid_size = len(self.grid)

    def _get_antinodes(self, recursive=False):
        antinodes = set()
        for node_positions in self.nodes.values():
            for node_1, node_2 in product(node_positions, repeat=2):
                if node_1 == node_2:
                    continue
                y1, x1 = node_1
                y2, x2 = node_2
                y_antinode = 2 * y2 - y1
                x_antinode = 2 * x2 - x1
                if recursive:
                    antinodes.add((y2, x2))
                while y_antinode in range(self.grid_size) and x_antinode in range(self.grid_size):
                    antinodes.add((y_antinode, x_antinode))
                    if not recursive:
                        break 
                    y1, x1, y2, x2 = y2, x2, y_antinode, x_antinode
                    y_antinode = 2 * y2 - y1
                    x_antinode = 2 * x2 - x1
        return antinodes
            
    def solve_first_part(self):
        return len(self._get_antinodes())
        
    def solve_second_part(self):
        return len(self._get_antinodes(recursive=True))
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')