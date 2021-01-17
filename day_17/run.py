#! /usr/bin/python3
from collections import Counter

# game of life - 3d
inputs = open('input.txt', 'r').read()
inputs = inputs.split('\n')

processed = set()

for x, _line in enumerate(inputs):
    for y, _char in enumerate(_line):
        if _char == '#':
            processed.add((x, y, 0))

loop = (-1, 0, 1)
for _ in range(6):
    _map_counter = Counter()
    for x, y, z in processed:
        for i in loop:
            for j in loop:
                for k in loop:
                    if i == j == k == 0:
                        continue
                    _map_counter[(x+i, y+j, z+k)] += 1
    new_pr = set()
    for _sets, _count in _map_counter.items():
        if _count == 3:
            new_pr.add(_sets)
    for _sets in processed:
        if _map_counter[_sets] in [2, 3]:
            new_pr.add(_sets)
    processed = new_pr

print(f'partOne:{len(processed)}')

# part two same with 4d
processed = set()

for x, _line in enumerate(inputs):
    for y, _char in enumerate(_line):
        if _char == '#':
            processed.add((x, y, z, 0))

loop = (-1, 0, 1)
for _ in range(6):
    _map_counter = Counter()
    for x, y, z, a in processed:
        for i in loop:
            for j in loop:
                for k in loop:
                    for l in loop:
                        if i == j == k == l == 0:
                            continue
                        _map_counter[(x+i, y+j, z+k, a+l)] += 1
    new_pr = set()
    for _sets, _count in _map_counter.items():
        if _count == 3:
            new_pr.add(_sets)
    for _sets in processed:
        if _map_counter[_sets] in [2, 3]:
            new_pr.add(_sets)
    processed = new_pr

print(f'partTwo:{len(processed)}')
