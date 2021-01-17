#! /usr/bin/python3


def parts(arr):
    arr.append(0)
    arr.append(max(arr)+3)
    arr.sort()
    _type1 = 0
    _type2 = 0
    for _x in range(0, len(arr)-1):
        _difference = arr[_x+1] - arr[_x]
        if _difference == 1:
            _type1 += 1
        elif _difference == 3:
            _type2 += 1

    _dict = {}

    def two(_index):
        if _index == len(arr) - 1:
            print('end return 1')
            return 1
        if _index in _dict:
            return _dict[_index]
        _sum = 0
        if _index + 1 < len(arr) and arr[_index+1] - arr[_index] <= 3:
            _sum += two(_index+1)
        if _index + 2 < len(arr) and arr[_index+2] - arr[_index] <= 3:
            _sum += two(_index+2)
        if _index + 3 < len(arr) and arr[_index+3] - arr[_index] <= 3:
            _sum += two(_index + 3)

        _dict[_index] = _sum
        return _sum
    print(f'partOne: {_type1*_type2}')
    print(arr)
    print(f'partTwo: {two(0)}')


inputs = [int(x.strip()) for x in open('input.txt', 'r').readlines()]
parts(inputs)
