import networkx as nx

class Solver:

    def __init__(self, *args, **kwargs):
        self.grid = {}
        self.start_positions = set()
        self.end_positions = set()
        self.graph = nx.DiGraph()
        with open('input.txt') as f:
            for y, line in enumerate(f):
                for x, value in enumerate(line.strip()):
                    self.graph.add_node((y, x))
                    value = int(value)
                    if value == 0:
                        self.start_positions.add((y, x))
                    elif value == 9:
                        self.end_positions.add((y, x))
                    self.grid[(y, x)] = int(value)
        # Add edges
        for (y, x), value in self.grid.items():
            for dy, dx in ((0, +1), (0, -1), (+1, 0), (-1, 0)):
                neighbor_coords = (y + dy, x + dx)
                neighbor_value = self.grid.get(neighbor_coords)
                if neighbor_value is None:
                    continue
                if neighbor_value == value + 1:
                    self.graph.add_edge((y, x), neighbor_coords)
        self.graph.remove_nodes_from(list(nx.isolates(self.graph)))

    def solve_first_part(self):
        path_ok = 0
        for start in self.start_positions:
            for end in self.end_positions:
                if nx.has_path(self.graph, start, end):
                    path_ok += 1
        return path_ok
        
    def solve_second_part(self):
        path_ok = 0
        for start in self.start_positions:
            for end in self.end_positions:
                path_ok += len(list(nx.all_simple_paths(self.graph, start, end)))
        return path_ok
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')