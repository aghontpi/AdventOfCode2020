#! /usr/bin/python3


def partOne(arr):
    preamble = 25
    for index in range(preamble, len(arr[preamble:])):
        value = arr[index]
        _tarr = arr[index - preamble: index + preamble]
        # each element after first five
        foundFlag = False
        for _index, _value in enumerate(_tarr):
            # prev five elements from previous loop untill last char -1
            _tarrr = arr[index+1 - preamble:index + 1 + preamble]
            for __index, __value in enumerate(_tarrr):
                # five elements after +1 from previous loop untill last char
                if _value == __value:
                    continue
                _sum = int(_value) + int(__value)
                if _sum == value:
                    foundFlag = True
        if not foundFlag:
            print(f"partone: {value}")
            exit()


def partTwo(arr):
    target = 257342611
    # one loop, since contiguous elements
    for i in range(0, len(arr) - 1):  # range of len -3, cuz future
        _tsum = 0
        _tarr = []
        _j = i + 1  # for looping untill end and before the target value
        while _tsum < target and _j < len(arr):
            _tarr.append(arr[_j])
            _tsum = sum(_tarr)
            _j += 1

        if _tsum == target:
            print(f"found: {max(_tarr) + min(_tarr)}")


inputs = [int(x.strip()) for x in open('input.txt', 'r').readlines()]
partTwo(inputs)
