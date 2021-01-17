#! /usr/bin/python3
import copy
_count_change = 0


def count_neighbour(arr, x, y, comp, partTwo=False):

    def withinbounds(xvalue, yvalue):
        flag = True
        if xvalue < 0 or xvalue >= _xmax:
            flag = False
        if yvalue < 0 or yvalue >= _ymax:
            flag = False
        return flag

    _count = 0
    for _i in range(-1, 2):
        for _j in range(-1, 2):
            xaxis = x + _i
            yaxis = y + _j
            if _i == 0 and _j == 0:
                continue
            # _xmax used in range is _xmax -1, so we check >= _xmax
            if xaxis < 0 or xaxis >= _xmax:
                continue
            if yaxis < 0 or yaxis >= _ymax:
                continue
            if not partTwo:
                element = arr[xaxis][yaxis]
                if element == comp:
                    _count += 1
            else:
                # check first occupied seat in each direction for part two
                while withinbounds(xaxis, yaxis) and arr[xaxis][yaxis] == '.':
                    xaxis += _i
                    yaxis += _j
                if withinbounds(xaxis, yaxis) and comp == arr[xaxis][yaxis]:
                    _count += 1
    return _count


def _count_seats(arr, part="partOne"):
    _count = 0
    for row in range(0, _xmax):
        for col in range(0, _ymax):
            if arr[row][col] == '#':
                _count += 1
    print(f'{part}: {_count}')


def pprint(arr):
    for _item in arr:
        print(''.join(_item))


def partOne(arr):
    global _count_change
    _clone = copy.deepcopy(arr)
    change = False
    # range goes from left -- inclusice, right -- exculsive
    # but arr index starts at 0 and ends to len(arr) - 1. if used with range,
    #  range is exclusive
    for row in range(0, _xmax):
        for col in range(0, _ymax):
            if arr[row][col] == 'L':
                _adjacent_seats_count = count_neighbour(arr, row, col, '#')
                if _adjacent_seats_count == 0:
                    _clone[row][col] = '#'
                    change = True
            if arr[row][col] == '#':
                _adjacent_seats_count = count_neighbour(arr, row, col, '#')
                if _adjacent_seats_count > 3:
                    _clone[row][col] = 'L'
                    change = True
    if change:
        _count_change += 1
        partOne(copy.deepcopy(_clone))
    else:
        print(f"changes: {_count_change}")
        _count_seats(_clone)


def partTwo(arr):
    global _count_change
    _clone = copy.deepcopy(arr)
    change = False
    # range goes from left -- inclusice, right -- exculsive
    # but arr index starts at 0 and ends to len(arr) - 1. if used with range,
    #  range is exclusive
    for row in range(0, _xmax):
        for col in range(0, _ymax):
            if arr[row][col] == 'L':
                _adjacent_seats_count = count_neighbour(
                    arr, row, col, '#', True)
                if _adjacent_seats_count == 0:
                    _clone[row][col] = '#'
                    change = True
            if arr[row][col] == '#':
                _adjacent_seats_count = count_neighbour(
                    arr, row, col, '#', True)
                if _adjacent_seats_count > 4:
                    _clone[row][col] = 'L'
                    change = True
    print('*' * 24)
    pprint(_clone)
    if change:
        partTwo(copy.deepcopy(_clone))
    else:
        _count_seats(_clone, 'partTwo')


inputs = [x.strip() for x in open('test.txt', 'r').readlines()]
_tmp = []
for _x in inputs:
    _x = list(_x)
    _tmp.append(_x)
inputs = _tmp
_xmax = len(inputs)
_ymax = len(inputs[0])
print(f"xmax: {_xmax}, ymax: {_ymax}")
partOne(inputs)
pprint(inputs)
partTwo(inputs)
