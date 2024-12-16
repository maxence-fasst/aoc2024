import networkx as nx

EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
NORTH = (-1, 0)
DIRECTIONS = (EAST, SOUTH, WEST, NORTH)

class Solver:

    def __init__(self, *args, **kwargs):
        self.grid = []
        self.start_position = None
        self.target = None
        self.graph = nx.DiGraph()
        with open('input.txt') as f:
            for y, line in enumerate(f):
                for x, value in enumerate(line.strip()):
                    if value == '#':
                        continue
                    self.grid.append((y, x))
                    if value == 'S':
                        self.start_position = (y, x, EAST)
                        self.graph.add_node((y, x, EAST))
                    else:
                        if value == 'E':
                            self.target = (y, x)
                        for direction in DIRECTIONS:
                            self.graph.add_node((y, x, direction))
                              
        # Add edges
        for (y, x, direction) in list(self.graph.nodes).copy():
            for dy, dx in DIRECTIONS:
                neighbor_coords = (y + dy, x + dx)
                neighbor_direction = (dy, dx)
                if neighbor_coords not in self.grid:
                    continue
                if direction == neighbor_direction:
                    self.graph.add_edge((y, x, direction), (y + dy, x + dx, direction), weight=1)
                else:
                    self.graph.add_edge((y, x, direction), (y + dy, x + dx, neighbor_direction), weight=1001)

    def solve_first_part(self):
        all_paths_length = []
        for direction in DIRECTIONS:
            target = self.target + (direction,)
            try:
                all_paths_length.append(nx.shortest_path_length(self.graph, self.start_position, target, weight='weight'))
            except:
                # No pass with target in this direction
                pass
        return min(all_paths_length)
        
    def solve_second_part(self):
        all_points = set()
        for direction in DIRECTIONS:
            target = self.target + (direction,)
            try:
                for path in nx.all_shortest_paths(self.graph, self.start_position, target, weight='weight'):
                    for point in path:
                        all_points.add(point[:2])
            except:
                # No pass with target in this direction
                pass
        return len(all_points) - 1
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')