import re

OPERATIONS = {
    'AND': '&',
    'OR': '|',
    'XOR': '^'
}

class Solver:

    def __init__(self, *args, **kwargs):
        self.data = {}
        wires_regex = re.compile(r"(.{3}): (\d)")
        operations_regex = re.compile(r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})")
        with open('input.txt') as f:
            for line in f.readlines():
                wires_regex_match = wires_regex.match(line)
                if wires_regex_match:
                    wire, value = wires_regex_match.groups()
                    self.data[wire] = bool(int(value))
                    continue
                operations_regex_match = operations_regex.match(line)
                if operations_regex_match:
                    wire1, operation, wire2, output = operations_regex_match.groups()
                    self.data[output] = (wire1, OPERATIONS[operation], wire2)

    def solve_first_part(self):
        result = {k: v for k, v in self.data.items() if isinstance(v, bool)}
        todo = {k: v for k, v in self.data.items() if not isinstance(v, bool)}
        while todo:
            possible_op = {k: v for k, v in todo.items() if v[0] in result and v[2] in result}
            for wire, value in possible_op.items():
                wire1, operation, wire2 = value
                result[wire] = eval(f'{result[wire1]} {operation} {result[wire2]}')
                del todo[wire]
        binary_value = ''.join([str(int(result[k])) for k in sorted(result.keys(), reverse=True) if k.startswith('z')])
        return int(binary_value, 2)
    
    def solve_second_part(self):
        pass


solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')