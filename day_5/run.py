#! /usr/bin/python3


def parts(arr):
    _max = 0
    _list = []
    for x in arr:
        row = x[0:7]
        col = x[7:10]
        row = row.replace('B', '1').replace('F', '0')
        col = col.replace('R', '1').replace('L', '0')
        uniqueid = (int(row, 2) * 8) + int(col, 2)
        _list.append(uniqueid)
        _max = max(_max, uniqueid)

    print(f'part-1: {_max}')
    _list.sort()
    for _item in _list:
        if _item-1 not in _list and _item+1 in _list:
            print(f'part-2: {_item-1}')


inputs = [x.strip() for x in open('input.txt', 'r').readlines()]
parts(inputs)
