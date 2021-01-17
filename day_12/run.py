#! /usr/bin/python3

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

# constrainsts
# ship starts at facing east
# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.

def partOne(arr):
    x = 0
    y = 0
    waypoint_x = 0
    waypoint_y = 0
    quadrants = [1, 1, -1, -1]
    facing_direction = 1
    # all calculations are based upon cardinal directions, north, east, south, west.
    for item in arr:
        # print(f"x: {x}, y: {y}")
        operation = item[0:1]
        value = int(item[1:])
        if operation == 'S':
            y -= value
        elif operation == 'N':
            y += value
        elif operation == 'E':
            x += value
        elif operation == 'W':
            x -= value
        elif operation == 'R':
            # 0 - 3, directions,
            facing_direction = (facing_direction + int(value/90)) % 4
        elif operation == 'L':
            facing_direction = (facing_direction - int(value/90)) % 4
        elif operation == 'F':
            if facing_direction == 1 or facing_direction == 3:
                x = quadrants[facing_direction] * value + x
            else:
                y = quadrants[facing_direction] * value + y
        else:
            assert False
    # since using graph, representation in two dimensional place, even if value is negative,
    # got to add up the two numbers
    print(x, y, abs(x)+abs(y))


def partTwo(arr):
    x = 0
    y = 0
    waypoint_x = 10  # east
    waypoint_y = 1  # north
    for item in arr:
        operation = item[0:1]
        value = int(item[1:])
        if operation == 'S':
            waypoint_y -= value
        elif operation == 'N':
            waypoint_y += value
        elif operation == 'E':
            waypoint_x += value
        elif operation == 'W':
            waypoint_x -= value
        elif operation == 'R':
            # 10 east, 4 north
            # r 90
            # 4 east, 10 south
            rotate = (int(value/90))
            for _ in range(rotate):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif operation == 'L':
            rotate = (int(value/90))
            for _ in range(rotate):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif operation == 'F':
            x = x + value * waypoint_y
            y = y + value * waypoint_x
        else:
            assert False
    # since using graph, representation in two dimensional place, even if value is negative,
    # got to add up the two numbers
    print(x, y, abs(x)+abs(y))


inputs = [x.strip() for x in open('input.txt', 'r')]
partOne(inputs)
partTwo(inputs)
