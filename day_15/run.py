#! /usr/bin/python3

# In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input).
#  Then, each turn consists of considering the most recently spoken number:

# If that was the first time the number has been spoken, the current player says 0.
# Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.


# For example, suppose the starting numbers are 0,3,6:

# Turn 1: The 1st number spoken is a starting number, 0.
# Turn 2: The 2nd number spoken is a starting number, 3.
# Turn 3: The 3rd number spoken is a starting number, 6.
# Turn 4: Now, consider the last number spoken, 6. Since that was the first time the number had been spoken, the 4th number spoken is 0.
# Turn 5: Next, again consider the last number spoken, 0. Since it had been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, 4) and the turn number of the time it was most recently spoken before then (turn 1). Thus, the 5th number spoken is 4 - 1, 3.
# Turn 6: The last number spoken, 3 had also been spoken before, most recently on turns 5 and 2. So, the 6th number spoken is 5 - 2, 3.
# Turn 7: Since 3 was just spoken twice in a row, and the last two turns are 1 turn apart, the 7th number spoken is 1.
# Turn 8: Since 1 is new, the 8th number spoken is 0.
# Turn 9: 0 was last spoken on turns 8 and 4, so the 9th number spoken is the difference between them, 4.
# Turn 10: 4 is new, so the 10th number spoken is 0.

from collections import defaultdict
spoken_list = []
mem_map = {}
# part one
# target = 2020
target = 30000000


def solution(arr):
    spoken_list = defaultdict(list)
    value = 0
    for _i in range(target):
        if _i < len(arr):
            value = arr[_i]
        elif len(spoken_list[value]) == 1:
            # previous spoken
            value = 0
        else:
            value = spoken_list[value][-1] - spoken_list[value][-2]
        spoken_list[value].append(_i)
    print('sol:', value)


inputs = open('input.txt', 'r').read()
inputs = [int(x.strip()) for x in inputs.split(',')]
solution(inputs)
