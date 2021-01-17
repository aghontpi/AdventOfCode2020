#! /usr/bin/python3

# FIRST TRY
import pprint
import re
from copy import deepcopy


# def parser(line, i, bracket):
#     ts = []
#     _char = line[i]
#     le = None
#     line_length = len(line) - 1

#     # preprocessing
#     _k = 0
#     while not bracket and _k <= line_length:
#         _xyz = line[_k]
#         _count = 0
#         if _xyz != '(':
#             ts.append(_xyz)
#         elif _xyz == "(":
#             [rs, _k] = parser(line, _k, True)
#             ts.append(rs)
#             if _k >= len(line) - 1:
#                 break
#         _k += 1

#     # bracket
#     while bracket and _char != ')' and i < line_length:
#         if _char == "(":
#             i += 1  # skip bracket
#             [re, i] = parser(line, i, True)
#             ts.append(re)  # replacing bracket stuff with calculated content
#             i = min(i+1, line_length)
#             # skip the closing bracket & update _char if not end of line
#             _char = line[i]
#             if i >= len(line) - 1:
#                 break
#         ts.append(_char)
#         i += 1
#         _char = line[i]
#     if bracket and _char != ')':  # last char after while loop
#         ts.append(_char)

#     print(f"items in parser: {ts}")

#     ri = None
#     op = None
#     for _item in ts:
#         # take on left operand initially,
#         # find operator,
#         # take on right operand
#         # if the right opearnd starts with bracket, process untill end of the bracket,

#         # try to parse as int
#         try:
#             _item = int(_item)
#         except:
#             pass
#         if le == None and isinstance(_item, int):
#             le = _item
#         elif _item == '+' or _item == '*':
#             op = _item
#         elif isinstance(_item, int):
#             ri = _item
#         # operator and right value are not set, continue untill they are set
#         if op == None or ri == None:
#             continue
#         try:
#             _eval_str = f"{le} {op} {ri}"
#             le = eval(_eval_str)
#             print(f"eval_str: {_eval_str}, le: {le}")
#         except:
#             print(f"error _eval, {_eval_str}")
#             exit(1)

#         # reset operator and right operand
#         op = None
#         ri = None
#     print(f'return {le}')
#     return [le, i]


# def partOne(arr):
#     rs = []
#     for line in arr:
#         print(line)
#         _r = parser(line, 0, False)
#         print(f"{_r[0]}")
#         rs.append(_r[0])
#     print(f"partOne: {sum(rs)}")

# TRY TWO


def parserTwo(line, _i, bracket):
    # assign left char, if the char is ( process the value by recursive call
    #  clean state, find till end of the bracket, return the data
    #  assign left, assign operand, assing right,  process  brackets untill these three are assigned

    _line_length = len(line)
    op = None
    _char = None
    left = None
    right = None
    while _i < _line_length:
        _char = line[_i]
        if _char == "(":
            _i += 1  # skip opening bracket
            [_char, _i] = parserTwo(line, _i, True)
        if _char == ")":
            return [left, _i]
        try:
            _char = int(_char)
        except:
            pass
        if isinstance(_char, int):
            if left == None:
                left = _char
            else:
                right = _char
        if _char == '+' or _char == '*':
            op = _char

        if op and left and right:
            try:
                _eval_str = f"{left} {op} {right}"
                left = eval(_eval_str)
                print(f"eval str: {_eval_str}")
            except:
                print(f'eval error : {_eval_str}')
            op = None
            right = None

        _i += 1

    return [left, _i]


def partOneTwo(arr):
    rs = []
    for line in arr:
        print(line)
        _r = parserTwo(line, 0, False)
        rs.append(_r[0])
    print(f"partOne: {sum(rs)}")


inputs = [x.strip().replace(' ', '')
          for x in open('input.txt', 'r').readlines()]
partOneTwo(deepcopy(inputs))

additionRegex = re.compile(r'(\d+) \+ (\d+)')


def calculateAllPlus(line):
    def add(match):
        # print('before plus rep', line)
        val = int(match[1]) + int(match[2])
        return str(val)
    while additionRegex.search(line):
        line = additionRegex.sub(add, line)
    # print('replace plus', line)
    return line


bracketRegex = re.compile(r'\(([^()]+)\)')


def process(match):
    if not isinstance(match, str):
        match = str(match[1])
    _tmp = match.split()
    left = _tmp[0]
    i = 1
    while i < len(_tmp):
        operator = _tmp[i]
        right = _tmp[i+1]
        if operator == '*':
            left = int(left) * int(right)
        elif operator == '+':
            left = int(left) + int(right)
        i += 2
    return str(left)


def process2(match):
    if not isinstance(match, str):
        match = str(match[1])
    match = calculateAllPlus(match)
    _tmp = match.split()
    left = _tmp[0]
    i = 1
    while i < len(_tmp):
        operator = _tmp[i]
        right = _tmp[i+1]
        if operator == '*':
            left = int(left) * int(right)
        elif operator == '+':
            left = int(left) + int(right)
        i += 2
    return str(left)


def calculateBracket(line, pt=False):
    # print('original line', line)
    while bracketRegex.search(line):
        if not pt:
            line = bracketRegex.sub(process, line)
        else:
            line = bracketRegex.sub(process2, line)
    # print('processed line', line)
    return line


def _partOne(arr):
    rs = []
    for line in arr:
        line = calculateBracket(line)
        line = int(process(line))
        rs.append(line)
    print(f"partOne: {sum(rs)}")


def _partTwo(arr):
    rs = []
    for line in arr:
        line = calculateBracket(line, True)
        line = int(process2(line))
        # print('ret', line)
        rs.append(line)
    print(f'partTwo: {sum(rs)}')


inputs = [x.strip()
          for x in open('input.txt', 'r').readlines()]
# _partOne(deepcopy(inputs))
_partTwo(deepcopy(inputs))
