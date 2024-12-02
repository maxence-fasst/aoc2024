import re

class Solver:

    def __init__(self, *args, **kwargs):
        self.list1 = []
        self.list2 = []
        regex = re.compile(r"(\d+)\s+(\d+)")
        with open('input.txt') as f:
            for line in f.readlines():
                number1, number2 = regex.findall(line.replace('\n', ''))[0]
                self.list1.append(int(number1))
                self.list2.append(int(number2))

    def solve_first_part(self):
        return sum([abs(x - y) for x, y in zip(sorted(self.list1), sorted(self.list2))])
    
    def solve_second_part(self):
        return sum(x * self.list2.count(x) for x in self.list1)


solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')