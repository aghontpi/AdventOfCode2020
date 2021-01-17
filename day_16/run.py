#! /usr/bin/python3
import pprint
import copy
_l = []

inputs = open('input.txt', 'r').read()
[possible_values, your_ticket, nearby_tickets] = inputs.split('\n\n')
possible_values = possible_values.split('\n')
for line in possible_values:
    _range = line.split(': ')[-1]
    _list = list(map(lambda x:  x.strip(), _range.split('or')))
    while _list:
        _it = _list.pop()
        [_st, _ed] = _it.split('-')
        _st = int(_st)
        _ed = int(_ed) + 1
        for _i in range(_st, _ed):
            if _i not in _l:
                _l.append(_i)


# partOne
nearby_tickets = nearby_tickets.split('\n')
nearby_tickets.pop(0)
not_valid = []

_nearby_valid_tickets = []  # for part two

for _x in nearby_tickets:
    _x = _x.split(',')
    valid = True
    for _i in _x:
        _i = int(_i)
        if _i not in _l:
            not_valid.append(_i)
            valid = False
    if valid:
        _nearby_valid_tickets.append(_x)
print(f"partOne : {sum(not_valid)}")


# partTwo

# based on valid conditions, find the order of the ticket order
# mul all orders that start with departure
valid_map = {}
for line in possible_values:
    [name, _range] = line.split(': ')
    _list = list(map(lambda x:  x.strip(), _range.split('or')))
    _name_valid_range = []
    while _list:
        _it = _list.pop(0)
        [_st, _ed] = _it.split('-')
        _st = int(_st)
        _ed = int(_ed) + 1
        for _i in range(_st, _ed):
            if _i not in _name_valid_range:
                _name_valid_range.append(_i)
    name = name.strip()
    valid_map[name] = _name_valid_range

map_keys = list(valid_map.keys())
possibilities = [copy.deepcopy(map_keys) for _i in map_keys]
your_ticket = your_ticket.split('\n')
your_ticket.pop(0)
your_ticket = [int(x.strip()) for x in your_ticket[0].split(',')]
_nearby_valid_tickets.append(your_ticket)


def removeInvalid(possibilities, j):
    i = 0
    while len(possibilities) != 1 and i < len(_nearby_valid_tickets):
        value = _nearby_valid_tickets[i][j]
        value = int(value)
        tmp = copy.deepcopy(map_keys)
        while tmp:
            item = tmp.pop(0)
            valid_items = valid_map[item]
            if value not in valid_items:
                _poss = copy.deepcopy(possibilities)
                if item in _poss:
                    del _poss[_poss.index(item)]
                    possibilities = _poss
        i += 1
    return possibilities


solved_map = {}
prev = None
for i in range(len(map_keys)):
    sol = removeInvalid(possibilities[i], i)
    solved_map[i] = set(sol)

finalSolvedMap = {}
while solved_map:
    for key, _set in list(solved_map.items()):
        if len(_set) == 1:
            _key, = _set
            finalSolvedMap[_key] = key
            solved_map.pop(key)
            for _value in solved_map.values():
                _value.discard(_key)

pdt = 1
for name, index in finalSolvedMap.items():
    if name.startswith('departure'):
        pdt = pdt * your_ticket[index]
print(f'partTwo: {pdt}')
