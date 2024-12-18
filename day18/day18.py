import networkx as nx

class Solver:

    def __init__(self, *args, **kwargs):
        grid_size = 71
        self.bytes_positions = []
        self.start = (0, 0)
        self.end = (70, 70)
        self.graph = nx.DiGraph()
        with open('input.txt') as f:
            for line in f.readlines():
                y, x = map(int, line.strip().split(','))
                self.bytes_positions.append((y, x))
        for y in range(grid_size):
            for x in range(grid_size):
                if (y, x) in self.bytes_positions[:1024]:
                    continue
                self.graph.add_node((y, x))
                for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_y, new_x = y + direction[0], x + direction[1]
                    if 0 <= new_y < grid_size and 0 <= new_x < grid_size and (new_y, new_x) not in self.bytes_positions[:1024]:
                        self.graph.add_edge((y, x), (new_y, new_x))
        

    def solve_first_part(self):
        return nx.shortest_path_length(self.graph, self.start, self.end)
        
    def solve_second_part(self):
        nodes_to_test = self.bytes_positions[1024:]
        while True:
            node = nodes_to_test.pop(0)
            self.graph.remove_node(node)
            if nx.has_path(self.graph, self.start, self.end):
                continue
            return f'{node[0]},{node[1]}'

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')