#! /usr/bin/python3
from copy import deepcopy

mem_map = {}
mask = ''

# python has inbuilt function to do this, but for practice
# doing it manually


def binary_conversion(_num):
    _bin = ''
    while _num:
        _rem = _num % 2
        if _rem == 1:
            _bin = '1' + _bin
        else:
            _bin = '0' + _bin
        _num = _num // 2
    return _bin


def decimal_conversion(_bin):
    _dec = 0
    _bin = list(_bin)
    _bin.reverse()
    for _i, _v in enumerate(_bin):
        _dec = _dec + int(_v) * pow(2, _i)

    return _dec


def pad_bits(_str, size=36):
    _len = len(_str)
    if _len == size:
        return _str
    while len(_str) < size:
        _str = '0' + _str
    return _str


def perform_mask(_bin):
    _bin = list(_bin)
    for _i, _bit in enumerate(list(mask)):
        if _bit == 'X':
            continue
        _bin[_i] = _bit
    _bin = ''.join(_bin)
    return _bin


def perform_mask_two(_bin):
    possible_bins = ['']
    _bin = list(_bin)
    for _i, _bit in enumerate(list(mask)):
        tmp = []
        for _itembin in possible_bins:
            _itembin = list(_itembin)
            if _bit == '0':
                _itembin.append(_bin[_i])
            elif _bit == '1':
                _itembin.append('1')
            elif _bit == 'X':
                _str = ''.join(_itembin)
                # collect all values of x
                tmp.append(_str + '0')
                tmp.append(_str + '1')
                continue
            _itembin = ''.join(_itembin)
            tmp.append(_itembin)
        possible_bins = deepcopy(tmp)
    return possible_bins


def parse_instruction(arr, partTwo=False):
    global mask
    if len(arr) < 1:
        return
    _mask = arr.pop(0)
    _mask = _mask.strip().replace('mask = ', '')
    mask = _mask
    _max = len(_mask)
    while arr:
        _inst = arr.pop(0)
        _inst = _inst.split('=')
        mem_loc = _inst[0].strip().replace('mem[', '').replace(']', '')
        mem_loc = int(mem_loc)
        if not partTwo:
            _value = int(_inst[1].strip())
            _original = pad_bits(binary_conversion(_value))
            _masked = perform_mask(_original)
            _dec = decimal_conversion(_masked)
            mem_map[mem_loc] = _dec
        else:
            _value = int(_inst[1].strip())
            _mem_ = int(mem_loc)
            _original = pad_bits(binary_conversion(_mem_))
            _masked = perform_mask_two(deepcopy(_original))
            for _mem in _masked:
                _mem_dec = decimal_conversion(_mem)
                mem_map[_mem_dec] = _value


def partOne(arr):
    tmp = []
    for _i, x in enumerate(arr):
        tmp.append(x)
        if _i+1 < len(arr) and arr[_i+1].__contains__('mask'):
            parse_instruction(tmp)
            tmp = []
    parse_instruction(tmp)
    total_sum = 0
    for _key in mem_map:
        total_sum += int(mem_map[_key])
    print(f'partOne: {total_sum}')


def partTwo(arr):
    tmp = []
    for _i, x in enumerate(arr):
        tmp.append(x)
        if _i+1 < len(arr) and arr[_i+1].__contains__('mask'):
            parse_instruction(tmp, True)
            tmp = []
    parse_instruction(tmp, True)
    total_sum = 0
    for _key in mem_map:
        total_sum += int(mem_map[_key])
    print(f'PartTwo: {total_sum}')


inputs = [x.strip() for x in open('input.txt', 'r').readlines()]
partOne(deepcopy(inputs))
mem_map = {}
partTwo(deepcopy(inputs))
