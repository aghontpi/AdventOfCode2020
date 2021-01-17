#! /usr/bin/python3

def partOne(arr):
    timeStamp = int(arr[0])
    busses = []
    tmp = [x for x in arr[1].split(',')]
    for x in tmp:
        if x != 'x':
            busses.append(int(x))
    maxTime = max(busses)
    calculateTimeStamp = timeStamp + maxTime
    # shortest waittime ?
    # find bus near timestamp
    busses.sort()
    sol = {}
    keys = []
    for y in busses:
        # only calculating the interval
        tmp = timeStamp - maxTime
        while tmp < calculateTimeStamp:
            tmp += 1
            if tmp % y == 0 and tmp > timeStamp:
                sol[tmp] = y
                keys.append(tmp)
    keys.sort()
    earliest_timestamp = keys.pop(0)
    bus = sol[earliest_timestamp]
    diff = earliest_timestamp - timeStamp
    print(bus, diff, bus*diff)


def partTwo(arr):
    # one gold coin for anyone that can find the earliest timestamp such that the first bus ID
    # departs at that time and each subsequent listed bus ID departs at that subsequent minute
    tmp = [x for x in arr[1].split(',')]
    _count = -1
    bus_map = {}
    busses = []
    for x in tmp:
        _count += 1
        if x == 'x':
            continue
        bus_map[int(x)] = _count
        busses.append(int(x))
    print(busses, bus_map)
    # timestamp where each bus is one minute appart
    # finding numbers in series, but the difference from each letters varies
    _counter = 0
    _rem = busses[0]
    # two values start at different. find point where there are subsequent
    for i, _b in enumerate(busses):
        if i + 1 == len(busses):
            break
        # next bus value
        _b = busses[i+1]
        while (_counter + bus_map[_b]) % _b != 0:
            _counter += _rem
        _rem = _rem * _b
        print(_b, _rem,  _counter)
    print("found", _counter)


inputs = [x.strip() for x in open('input.txt', 'r').readlines()]
# partOne(inputs)
partTwo(inputs)
