from itertools import cycle
from collections import defaultdict

NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'

DIRECTIONS = {
    NORTH: (-1, 0),
    EAST: (0, 1),
    SOUTH: (1, 0),
    WEST: (0, -1)
}

NEXT_MOVES = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

class Solver:

    def __init__(self, *args, **kwargs):
        self.grid = []
        with open('input.txt') as f:
            for i, line in enumerate(f.readlines()):
                line = line.replace('\n', '')
                self.grid.append(line)
                if NORTH in line:
                    self.start_position = (i, int(line.index(NORTH)))    

    def _get_all_moves(self, block=None):
        MOVE_ORDER = cycle([NORTH, EAST, SOUTH, WEST])
        actual_pos = self.start_position
        actual_direction = next(MOVE_ORDER)
        moves = defaultdict(set)
        moves[actual_direction].add(self.start_position)
        while True:
            try:
                move = DIRECTIONS[actual_direction]
                next_pos = (actual_pos[0] + move[0], actual_pos[1] + move[1])
                next_y, next_x = next_pos
                if next_y < 0 or next_x < 0:
                    break
                next_char = self.grid[next_pos[0]][next_pos[1]]
                if next_char == '#' or next_pos == block:
                    actual_direction = next(MOVE_ORDER)
                    continue
                if block and next_pos in moves[actual_direction]:
                    # Cycle detected
                    return
                moves[actual_direction].add(next_pos)
                actual_pos = next_pos
            except IndexError:
                break
        return moves

    def solve_first_part(self):
        moves = self._get_all_moves()
        return len(moves[NORTH] | moves[EAST] | moves[SOUTH] | moves[WEST])

    def solve_second_part(self):
        moves = self._get_all_moves()
        all_moves =  (moves[NORTH] | moves[EAST] | moves[SOUTH] | moves[WEST]) - {self.start_position}
        return sum(not self._get_all_moves(block=move) for move in all_moves)
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')