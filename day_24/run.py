#! /usr/bin/python3

inputs = open('input.txt', 'r').read()
inputs = inputs.split('\n')[0:-1]
# hexgrid coordinate system based on cardinal directions
# mentioned directions e, se, sw, w, nw, and ne
coordinate_system = {
    'e': {'x': 1, 'y': -1, 'z': 0},
    'se': {'x': 0, 'y': -1, 'z': +1},
    'sw': {'x': -1, 'y': 0, 'z': +1},
    'w': {'x': -1, 'y': +1, 'z': 0},
    'nw': {'x': 0, 'y': +1, 'z': -1},
    'ne': {'x': 1, 'y': 0, 'z': -1},
}

# hashmap to maintain the tiles
white_tiles = set()
black_tiles = set()


for line in inputs:
    _value = None
    while line:
        _direction = line[0:1]
        if _direction in coordinate_system:
            _direction = line[0:1]
            line = line[1:]
        else:
            _direction = line[0:2]
            line = line[2:]
        _dir = coordinate_system[_direction]
        _x, _y, _z = _dir['x'], _dir['y'], _dir['z']
        if _value:
            x, y, z = _value
        # x, y, z = _value if _value else 0, 0, 0
        else:
            x, y, z = 0, 0, 0
        x, y, z = x + _x, y + _y, z + _z
        _value = (x, y, z)

    if _value not in black_tiles and _value not in white_tiles:
        # they begin with white tiles
        white_tiles.add(_value)
    elif _value in white_tiles:
        white_tiles.remove(_value)
        black_tiles.add(_value)
    elif _value in black_tiles:
        black_tiles.remove(_value)
        white_tiles.add(_value)
print(f'partOne :{len(white_tiles)}')

for _ in range(100):
    tmp = set()
    itemsToCheck = set()
    for tile in white_tiles:
        x, y, z = tile
        itemsToCheck.add((x, y, z))
        for _dir in coordinate_system.values():
            _x, _y, _z = _dir.values()
            itemsToCheck.add((x+_x, y+_y, z+_z))
    for tile in itemsToCheck:
        _count = 0
        x, y, z = tile
        for _dir in coordinate_system.values():
            _x, _y, _z = _dir.values()
            if (x+_x, y+_y, z+_z) in white_tiles:
                _count += 1
        if (x, y, z) in white_tiles and (_count == 1 or _count == 2):
            tmp.add((x, y, z))
        if (x, y, z) not in white_tiles and _count == 2:
            tmp.add((x, y, z))
    white_tiles = tmp

print(f'partTwo :{len(white_tiles)}')
