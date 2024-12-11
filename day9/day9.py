from itertools import cycle
from collections import defaultdict

FILE = 'file'
FREESPACE = 'freespace'
MOVED = 'moved'

class Item:
    
    def __init__(self, type, value, size=0):
        self.type = type
        self.value = value
        self.size = int(size)

    def __repr__(self):
        return f'{self.type}({self.value}, {self.size})'
           

class Solver:

    def __init__(self, *args, **kwargs):
        self.data = defaultdict(str)
        entry_types = cycle([FILE, FREESPACE])
        with open('input.txt') as f:
            for number in f.read():
                entry_type = next(entry_types)
                self.data[entry_type] += number
        self.data[FREESPACE] = self.data[FREESPACE] + '0'

    def _get_blocks(self, group_by_block=False):
        blocks = []
        for i, (nb_file, nb_freespace) in enumerate(zip(self.data[FILE], self.data[FREESPACE])):
            if group_by_block:
                blocks.append(Item(FILE, i, nb_file))
                blocks.append(Item(FREESPACE, i, nb_freespace))
            else:
                blocks.extend([Item(FILE, i) for _ in range(int(nb_file))])
                blocks.extend([Item(FREESPACE, 0) for _ in range(int(nb_freespace))])
        return blocks
            
    def solve_first_part(self):
        blocks = self._get_blocks()
        files = [b for b in blocks if b.type == FILE]
        len_files = len(files)
        checksum = []
        for item in blocks:
            if item.type == FILE:
                checksum.append(item)
            else:
                checksum.append(files.pop())
            if len(checksum) == len_files:
                break
        return sum([i * item.value for i, item in enumerate(checksum)])
            
    def solve_second_part(self):
        blocks = self._get_blocks(group_by_block=True)
        for i in range(len(blocks), 0, -1):
            item = blocks[i - 1]
            if item.type in [FREESPACE, MOVED]:
                continue
            # find free space available
            for j, item2 in enumerate(blocks):
                if j == i: 
                    break
                if item2.type == FREESPACE and item2.size >= item.size:
                    # Replace item by MOVED
                    moved = Item(MOVED, item.value, item.size)
                    blocks[blocks.index(item)] = moved
                    updated_free_space = Item(FREESPACE, item2.value, item2.size - item.size)
                    del blocks[j]
                    if updated_free_space.size > 0:
                        blocks.insert(j, updated_free_space)      
                    blocks.insert(j, item)
                    break
        result = 0
        real_index = 0
        for item in [b for b in blocks if b.size > 0]:
            for _ in range(item.size):
                if item.type == FILE:
                    result += real_index * item.value
                real_index += 1
        return result
                

solver = Solver()
print(f'Solution 1 = {solver.solve_first_part()}')
print(f'Solution 2 = {solver.solve_second_part()}') 
