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

class Solver:

    def __init__(self, *args, **kwargs):
        self.robot = None
        self.walls = []
        self.boxes = []
        self.moves = ''
        with open('input.txt') as f:
            for i, line in enumerate(f.readlines()):
                line = line.replace('\n', '')
                if not line:
                    continue
                if '#' in line:
                    for j, char in enumerate(line):
                        if char == '#':
                            self.walls.append((i, j))
                        elif char == 'O':
                            self.boxes.append((i, j))
                        elif char == '@':
                            self.robot = (i, j)
                else:
                    self.moves += line

    def _get_boxes_to_move(self, by, bx, direction):
        boxes_copy = self.boxes.copy()
        boxes_to_move = [boxes_copy.pop(boxes_copy.index((by, bx)))]
        while True:
            by, bx = by + DIRECTIONS[direction][0], bx + DIRECTIONS[direction][1]
            if (by, bx) in self.walls:
                return []
            if (by, bx) in boxes_copy:
                boxes_to_move.append(boxes_copy.pop(boxes_copy.index((by, bx))))
            else:
                self.boxes = boxes_copy
                return boxes_to_move

    def _move(self, direction):
        yr, xr = self.robot
        next_y, next_x = (yr + DIRECTIONS[direction][0], xr + DIRECTIONS[direction][1])
        # Wall
        if (next_y, next_x) in self.walls:
            return
        
        # Box
        if (next_y, next_x) in self.boxes:
            boxes_to_move = self._get_boxes_to_move(next_y, next_x, direction)
            for (by, bx) in boxes_to_move:
                self.boxes.append((by + DIRECTIONS[direction][0], bx + DIRECTIONS[direction][1]))
            if boxes_to_move:
                self.robot = (next_y, next_x)
            return

        # Open space
        self.robot = (next_y, next_x)
        return
    
    def solve_first_part(self):
        for move in self.moves:
            self._move(move)
        return sum(y * 100 + x for y, x in self.boxes)
    
    def solve_second_part(self):
        pass
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')