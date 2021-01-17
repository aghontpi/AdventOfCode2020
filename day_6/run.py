#! /usr/bin/python3


def parts(arr):
    _sum = 0
    _sum2 = 0
    for x in arr:
        x = x.splitlines()
        questions = []
        answered = []
        for y in x:
            for _char in y:
                # part 1
                if _char not in questions:
                    questions.append(_char)
                # part 2
                person_answered = True
                for xy in x:
                    if _char not in xy:
                        person_answered = False
                        break
                if person_answered:
                    if _char not in answered:
                        _sum2 += 1
                        answered.append(_char)
        _sum += len(questions)
    print(f"part one: {_sum}")
    print(f"part two: {_sum2}")


inputs = open('inputs.txt', 'r').read()
inputs = inputs.split('\n\n')
parts(inputs)
