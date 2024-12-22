import networkx as nx
from collections import defaultdict

class Solver:

    def __init__(self, *args, **kwargs):
        self.grid = []
        self.start = None
        self.end = None
        self.walls = []
        self.graph = nx.DiGraph()
        with open('input.txt') as f:
            for y, line in enumerate(f.readlines()):
                self.grid.append(line.strip())
                for x, char in enumerate(line.strip()):
                    if char == '#':
                        self.walls.append((y, x))
                        continue
                    self.graph.add_node((y, x))
                    if char == 'S':
                        self.start = (y, x)
                    elif char == 'E':
                        self.end = (y, x)
        self.walls = [(y, x) for y, x in self.walls if y > 0 and x > 0 and y < len(self.grid) - 1 and x < len(self.grid[0]) - 1]         
        for y, x in self.graph.nodes:
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_y, new_x = y + direction[0], x + direction[1]
                if (new_y, new_x) in self.graph.nodes:
                    self.graph.add_edge((y, x), (new_y, new_x))
        self.initial_path = nx.shortest_path(self.graph, self.start, self.end)

    def _new_graph_from_initial(self):
        new_graph = nx.DiGraph()
        for y, x in self.initial_path:
            new_graph.add_node((y, x))
        for y, x in self.initial_path:
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_y, new_x = y + direction[0], x + direction[1]
                if (new_y, new_x) in new_graph.nodes:
                    new_graph.add_edge((y, x), (new_y, new_x))
        return new_graph
        
    def solve_first_part(self):
        done = set()
        result = 0
        initial_length = len(self.initial_path) - 1
        path_walls = []
        for (y, x) in self.walls:
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_y, next_x = y + direction[0], x + direction[1]
                if (next_y, next_x) in self.initial_path:
                    path_walls.append((y, x))
                    break
        for y, x in path_walls:
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_y, next_x = y + direction[0], x + direction[1]
                sorted_coords = sorted([(y, x), (next_y, next_x)])
                sorted_coords_str = ','.join([str(coord) for coord in sorted_coords])
                if sorted_coords_str in done:
                    continue
                done.add(sorted_coords_str)
                new_graph = self._new_graph_from_initial()
                new_graph.add_nodes_from([(y, x), (next_y, next_x)])
                for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    dy, dx = y + direction[0], x + direction[1]
                    if (dy, dx) in new_graph.nodes:
                        new_graph.add_edge((y, x), (dy, dx))
                    ndy, ndx = next_y + direction[0], next_x + direction[1]
                    if (ndy, ndx) in new_graph.nodes:
                        new_graph.add_edge((next_y, next_x), (ndy, ndx))
                if nx.has_path(new_graph, self.start, self.end):
                    new_length = nx.shortest_path_length(new_graph, self.start, self.end)
                    if new_length < initial_length and initial_length - new_length >= 100:
                        result += 1
        return result
        
    def solve_second_part(self):
        pass

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')