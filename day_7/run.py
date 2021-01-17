#! /usr/bin/python3
from collections import deque


def parts(arr):
    count = 0
    _map = {}
    count2 = 0
    # parse and map
    for x in arr:
        x = x.replace('bags', '').replace(
            'bag', '')
        x = list(map(lambda x: x.strip(), x.split('contain')))
        if x[1].__contains__(','):
            _tmp = list(map(lambda x: x.strip().strip(' .'), x[1].split(',')))
            x[1] = _tmp
        else:
            x[1] = x[1].strip(' .')
            x[1] = [x[1]]
        _map[x[0]] = x[1]

    def _is_gold(_x):
        _queue = deque()
        _queue.append(_x)
        while _queue:
            _tmp = _queue.popleft()
            if _tmp != 'no other':
                _tmp = _tmp[2:]
                for _y in _map[_tmp]:
                    _queue.append(_y)

            if _tmp == 'shiny gold':
                return True
        return False

    for _item in _map:
        for _x in _map[_item]:
            if _is_gold(_x):
                count += 1
                break

    # process inputs for second part
    for _item in _map:
        _pr = []
        for _tmp in _map[_item]:
            if _tmp == 'no other':
                c = 0
                n = _tmp
            else:
                n = _tmp[2:]
                c = int(_tmp[0:1])
            _pr.append({'count': c, 'name': n})
        _map[_item] = _pr

    def _count_bags(item_list):
        _sum = 0
        for item in item_list:
            _count = item['count']
            _bag = item['name']
            if _bag != 'no other':
                _sum = _sum + _count + _count * _count_bags(_map[_bag])
        print('return sum', _sum)
        return _sum

    count2 = _count_bags(_map['shiny gold'])
    print(f"partOne: {count}")
    print(f"partTwo: {count2}")


inputs = [x.strip() for x in open('inputs.txt', 'r')]
parts(inputs)
