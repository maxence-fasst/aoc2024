from collections import defaultdict

LOCKS = '#'
KEYS = '.'

class Solver:

    def __init__(self, *args, **kwargs):
        data = defaultdict(list)
        with open('input.txt') as f:
            actual = []
            for line in [l.strip() for l in f.readlines()]:
                if not line:
                    if actual:
                        actual_type = LOCKS if actual[0].startswith(LOCKS) else KEYS
                        data[actual_type].append(actual)
                        actual = []
                    continue
                actual.append(line) 
            actual_type = LOCKS if actual[0].startswith(LOCKS) else KEYS
            data[actual_type].append(actual)
        self.locks = [self._get_pin_heights(item, LOCKS) for item in data[LOCKS]]
        self.keys = [self._get_pin_heights(item, KEYS) for item in data[KEYS]]

    def _get_pin_heights(self, item, item_type):
        def _find_value(line, item_type):
            search = LOCKS if item_type == KEYS else KEYS
            result = list(line).index(search) if search in line else 5
            return result if item_type == LOCKS else 5 - result
        transposed = list(zip(*item[1:-1]))
        return [_find_value(line, item_type) for line in transposed]
    
    def _fit(self, lock, key):
        return all([l + k <= 5 for l, k in zip(lock, key)])

    def solve_first_part(self):
        return sum([self._fit(lock, key) for lock in self.locks for key in self.keys])
    
    def solve_second_part(self):
        return 'Merry Christmas!'


solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')