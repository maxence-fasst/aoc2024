from collections import defaultdict

class Solver:
    def __init__(self, *args, **kwargs):
        self.pairs = []
        self.updates = []
        rules_done = False
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if not line:
                    rules_done = True
                    continue
                if not rules_done:
                    a, b = line.split('|')
                    self.pairs.append((int(a), int(b)))
                    continue
                self.updates.append([int(e) for e in line.split(',')])

    def _get_antecedents(self, pairs):
        d = defaultdict(set)
        for a, b in pairs:
            d[b].add(a)
        return d
    
    def _is_ordered(self, update_to_check, all_antecedents):
        update = update_to_check.copy()
        while update:
            element = update.pop(0)
            antecedents = all_antecedents.get(element)
            if not antecedents:
                continue
            if len(update) != len(set(update) - antecedents):
                return False
        else:
            return True
            
    def _get_checked_updates(self):
        all_antecedents = self._get_antecedents(self.pairs)
        updates_ok = []
        updates_ko = []
        for update in self.updates:
            if self._is_ordered(update, all_antecedents):
                updates_ok.append(update)
            else:
                updates_ko.append(update)
        return updates_ok, updates_ko

    def solve_first_part(self):
        updates_ok, _ = self._get_checked_updates()
        return sum(update[len(update) // 2] for update in updates_ok)
    
    def solve_second_part(self):
        result = 0
        _, updates_ko = self._get_checked_updates()
        all_antecedents = self._get_antecedents(self.pairs)
        for base_update in updates_ko:
            nb_antecedents = defaultdict(int)
            update = base_update.copy()
            while update:
                element = update.pop()
                antecedents = all_antecedents.get(element, set())
                nb_antecedents[element] += len(set(base_update) - antecedents)
            ordered = {v: k for k, v in nb_antecedents.items()}
            ordered = [ordered[k] for k in sorted(ordered.keys(), reverse=True)]
            result += ordered[len(ordered) // 2]
        return result
       
        
solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}')