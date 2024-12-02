import re

class Solver:

    def __init__(self, *args, **kwargs):
        self.reports = []
        with open('input.txt') as f:
            for line in f.readlines():
                numbers = line.replace('\n', '').split(' ')
                self.reports.append([int(n) for n in numbers])

    def _report_is_valid(self, report):
        # Increasing or decreasing
        if report not in [sorted(report), sorted(report, reverse=True)]:
            return False
        for number1, number2 in [(report[i], report[i + 1]) for i in range(0, len(report) - 1, 1)]:
            diff = abs(number1 - number2)
            if diff not in [1, 2, 3]:
                return False
        return True
    
    def _report_is_valid_with_removed_element(self, report):
        for i in range(len(report)):
            if self._report_is_valid(report[:i] + report[i + 1:]):
                return True
        return False
        
    def solve_first_part(self):
        return len([report for report in self.reports if self._report_is_valid(report)])
    
    def solve_second_part(self):
        result = 0
        bad_reports = []
        for report in self.reports:
            if self._report_is_valid(report):
                result += 1
            else:
                bad_reports.append(report)
        return result + len([report for report in bad_reports if self._report_is_valid_with_removed_element(report)])
        

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')