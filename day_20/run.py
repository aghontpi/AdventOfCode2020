#!/usr/bin/python3
import math
import pprint

input_size = 0
count_roughness = 0


class Tile:
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid


def flip(item):
    # print(f'flip - original :\n {item}')
    flipped = [[0 for x in range(10)] for y in range(10)]
    item = item.split('\n')
    size = len(item) - 1
    for i in range(0, len(item)):
        _item = item[i]
        _item = list(_item)
        for j in range(0, len(_item)):
            flipped[i][j] = item[i][size-j]
    _len = len(flipped)
    tmp = []
    for i in range(_len):
        _prse = ''.join(map(str, flipped[i]))
        if i != _len - 1:
            _prse += '\n'
        tmp.append(_prse)
    flipped = ''.join(tmp)
    # print(f"flipped: \n{flipped}")
    return flipped


def rotate(item):
    # print(f'rotate - original :\n {item}')
    rotated = [[0 for x in range(10)] for y in range(10)]
    item = item.split('\n')
    size = len(item) - 1
    orinigal = []
    for _x in item:
        orinigal.append(list(_x))

    for i in range(0, len(item)):
        _item = item[i]
        _item = list(_item)
        for j in range(0, len(_item)):
            rotated[i][j] = orinigal[size-j][i]
    tmp = []
    _len = len(rotated)
    for i in range(_len):
        _prse = ''.join(map(str, rotated[i]))
        if i != _len - 1:
            _prse += '\n'
        tmp.append(_prse)
    rotated = ''.join(tmp)
    # print(f'rotated :\n {rotated}')
    return rotated


def isDown(a, b):
    a = a.split('\n')
    b = b.split('\n')
    _max = len(a) - 1
    return a[_max] == b[0]


def isRight(a, b):
    a = a.split('\n')
    b = b.split('\n')
    _max = len(a) - 1
    for row in range(0, len(a)):
        if a[row][_max] != b[row][0]:
            return False
    return True


def findPatternMonster(grid):
    global sea_monster
    global count_roughness
    monster_height = len(sea_monster)
    monster_width = len(sea_monster[0])
    size = len(grid)
    row = 0
    column = 0
    while row + monster_height - 1 < size:
        column = 0
        while column + monster_width - 1 < size:
            found = True
            i = j = 0
            while i < monster_height:
                j = 0
                while j < monster_width:
                    if sea_monster[i][j] == '#' and grid[row + i][column+j] == '.':
                        found = False
                    j += 1
                i += 1
            if not found:
                column += 1
                continue
            i = j = 0
            while i < monster_height:
                j = 0
                while j < monster_width:
                    if sea_monster[i][j] == '#':
                        _row = list(grid[row+i])
                        _row[column+j] = 'O'
                        grid[row+i] = ''.join(_row)
                    j += 1
                i += 1
            column += 1
        row += 1
    for row in grid:
        for cell in row:
            if cell == '#':
                count_roughness += 1


def removeCornersEdges():
    global result
    processed = []
    size = 10
    row = 0
    col = 0
    while row < input_size * size:
        if row % size == 0 or row % size == size-1:
            row += 1
            continue
        line = []
        col = 0
        while col < input_size * size:
            if col % size == 0 or col % size == size-1:
                col += 1
                continue
            tile = result[row//size][col//size]
            grid = tile.grid
            grid = grid.split('\n')
            _char = grid[row % size][col % size]
            line.append(_char)
            col += 1
        processed.append(''.join(line))
        row += 1
    # rows and columns must be equal
    assert(len(processed) == len(processed[0]))
    findPatternMonster(processed)


def search(row, col, used):
    global result
    global count_roughness
    if row == input_size:
        left = result[0][0]
        right = result[0][input_size-1]
        downleft = result[input_size-1][0]
        downright = result[input_size - 1][input_size-1]
        removeCornersEdges()
        print(
            f'tl: {left.id}, tr: {right.id}, dl: {downleft.id}, dr: {downright.id}')
        print(f'partOne: {left.id * right.id * downleft.id * downright.id}')
        print(f'partTwo:{count_roughness}')
        exit()
    for tile in possible_tile_arr:
        if tile.id not in used:
            if row > 0 and not isDown((result[row-1][col]).grid, tile.grid):
                continue
            if col > 0 and not isRight((result[row][col-1]).grid, tile.grid):
                continue
            result[row][col] = tile
            used.add(tile.id)
            if (col == input_size - 1):
                search(row + 1, 0, used)
            else:
                search(row, col + 1, used)
            # if the item in it current rotate/flip position is not correct then remove the item
            used.remove(tile.id)


inputs = open('test.txt', 'r').read()
inputs = inputs.split('\n\n')
# map with inputs
input_map = {}
for section in inputs:
    _section = section.split('\n')
    tile = _section.pop(0)
    _section = "\n".join(_section)
    tile = tile.replace('Tile ', '').replace(':', '')
    tile = int(tile)
    input_map[tile] = _section

possible_tile_arr = []
for x in input_map:
    # all possbile combinations
    # can be flipped 2 times
    # can be rotated 4 times
    i = 0
    process = input_map[x]
    while i < 2:
        j = 0
        while j < 4:
            possible_tile_arr.append(Tile(x, process))
            process = rotate(process)
            j += 1
        process = flip(process)
        i += 1

input_size = math.floor(math.sqrt((possible_tile_arr.__len__()/8)))
result = [[None for x in range(0, input_size+1)]
          for y in range(0, input_size+1)]
sea_monster = open('sea_monster', 'r').read().split('\n')
used = set()
search(0, 0, used)
