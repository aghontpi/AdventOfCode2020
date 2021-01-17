#! /usr/bin/python3
from var_dump import var_dump
from copy import deepcopy
from collections import defaultdict
food = []
allergies_map = defaultdict(set)
recipes_map = defaultdict(list)


def partOne(arr):
    for _index, x in enumerate(arr):
        tmp = x[x.index('(')+1:x.index(')')]
        tmp = tmp.replace('contains ', '')
        allergies = []
        for _y in tmp.split(','):
            _y = _y.strip()
            allergies.append(_y)
        allergies = set(allergies)
        x = x[0: x.index(' ('):]
        ingredients = set(x.split(' '))
        food.append(ingredients)
        for _allergy in allergies:
            recipes_map[_allergy].append(_index)
        for _ingredients in ingredients:
            allergies_map[_ingredients] |= allergies

    ans = []

    for __ingredients, _contains in allergies_map.items():
        _contains = allergies_map[__ingredients]
        _not_contains = set()
        for __allergy in _contains:
            for _i in recipes_map[__allergy]:
                if __ingredients not in food[_i]:
                    _not_contains.add(_allergy)
                    break
        _contains -= _not_contains

        if not _contains:
            ans.append(__ingredients)

    _sum = 0
    for _ingred in ans:
        tot += sum(_ingred in r for r in food)

    print(_sum)

# second try - based on sets


inputs = open('input.txt', 'r').readlines()
# partOne(inputs)
allergies_map = {}
ingredients_list = []

for x in inputs:
    allergies = []
    ingredients = set()
    # parsing
    tmp = x[x.index('(')+1:x.index(')')].replace('contains ', '')
    for _y in tmp.split(','):
        _y = _y.strip()
        allergies.append(_y)
    x = x[0: x.index(' ('):]
    ingredients = set(x.split(' '))
    ingredients_list.extend(ingredients)

    # processing
    for allergy in allergies:
        if allergy not in allergies_map:
            allergies_map[allergy] = ingredients
        else:
            _t_map = allergies_map[allergy]
            _t_map = _t_map.intersection(ingredients)
            allergies_map[allergy] = _t_map

found = {}
while allergies_map:
    for _allergy, _ingredient in list(allergies_map.items()):
        if len(_ingredient) == 1:
            _val, = _ingredient
            found[_allergy] = _val
            del allergies_map[_allergy]
            for _items in allergies_map.values():
                _items.discard(_val)
_sum = 0
for x in ingredients_list:
    if x not in found.values():
        _sum += 1
print(f'partOne: {_sum}')


_alphabetical_order = []
for x in sorted(found.keys()):
    _alphabetical_order.append(found[x])
print(f'partTwo: {",".join(_alphabetical_order)}')
