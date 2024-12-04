import re
import itertools

class Solver:

    def __init__(self, *args, **kwargs):
        self.data = []
        with open('input.txt') as f:
            for line in f.readlines():
                self.data.append(line.replace('\n', ''))

    def solve_first_part(self):
        # Horizontal
        all_strings = self.data.copy()

        # Vertical
        str_len = len(all_strings[0])
        for j in range(str_len):
            all_strings.append(''.join(s[j] for s in self.data))
        
        len_x = len(self.data[0])
        len_y = len(self.data)
        # Diagonals 
        for _, coords in itertools.groupby(sorted(itertools.product(range(len_x), range(len_y)), key=sum), key=sum):
            coords = list(coords)
            if len(coords) < 4:
                continue
            all_strings.append(''.join(self.data[y][x] for x, y in coords))
            all_strings.append(''.join(self.data[y][len_x - x - 1] for x, y in coords))

        regex = re.compile(r"(?=(XMAS|SAMX))")
        return len(regex.findall('_'.join(all_strings)))
    
    
    def solve_second_part(self):
        all_squares = []
        for i in range(len(self.data) - 2):
            for j in range(len(self.data[0]) - 2):
                square = []
                for x in range(3):
                    square.append(self.data[i + x][j:j + 3])
                all_squares.append(square)
        result = 0
        for square in all_squares:
            first_diag = square[0][0] + square[1][1] + square[2][2]
            second_diag = square[0][2] + square[1][1] + square[2][0]
            regex = re.compile(r"MAS|SAM")
            if regex.match(first_diag) and regex.match(second_diag):
                result += 1
        return result


solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')