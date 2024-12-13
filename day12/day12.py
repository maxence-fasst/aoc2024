class Solver:

    def __init__(self, *args, **kwargs):
        with open('input.txt') as f:
            self.grid = [line.replace('\n', '') for line in f.readlines()]
        self.regions = self._find_regions(self.grid)

    def _find_regions(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        regions = []

        def dfs(x, y, value):
            stack = [(x, y)]
            region = []
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < rows and 0 <= cy < cols and not visited[cx][cy] and grid[cx][cy] == value:
                    visited[cx][cy] = True
                    region.append((cx, cy))
                    stack.extend([(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)])  # 4-voisins
            return region

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    region = dfs(i, j, grid[i][j])
                    if region:
                        regions.append(region)
        return regions

    def solve_first_part(self):
        result = 0
        for region in self.regions:
            perimeter = 0
            for x, y in region:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in region:
                        continue
                    perimeter += 1
            result += perimeter * len(region)
        return result
    
    def solve_second_part(self):
        result = 0
        for region in self.regions:
            corners = 0
            # Thx @debnet <3
            for x, y in region:
                # Outer corners
                corners += (x-1, y) not in region and (x, y-1) not in region
                corners += (x+1, y) not in region and (x, y-1) not in region
                corners += (x-1, y) not in region and (x, y+1) not in region
                corners += (x+1, y) not in region and (x, y+1) not in region
                # Inner corners
                corners += (x-1, y) in region and (x, y-1) in region and (x-1, y-1) not in region
                corners += (x+1, y) in region and (x, y-1) in region and (x+1, y-1) not in region
                corners += (x-1, y) in region and (x, y+1) in region and (x-1, y+1) not in region
                corners += (x+1, y) in region and (x, y+1) in region and (x+1, y+1) not in region
            result += corners * len(region)
        return result
       
        
solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')