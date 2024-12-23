import networkx as nx

class Solver:

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            data = [line.strip().split('-') for line in f.readlines()]
        self.graph = nx.Graph(data)
        
    def solve_first_part(self):
        three_connected_computers = [c for c in nx.enumerate_all_cliques(self.graph) if len(c) == 3]
        return sum([any(c.startswith('t') for c in computers) for computers in three_connected_computers])
        
    def solve_second_part(self):
       max_linked_computers = nx.graph_clique_number(self.graph)
       computers = [c for c in nx.enumerate_all_cliques(self.graph) if len(c) == max_linked_computers][0]
       return ','.join(sorted(computers))

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')