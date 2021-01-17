#! /usr/bin/python3

def executor(_x, _i, acc):
    _name = _x[0:3]
    _value = int(_x[4:])
    if _name == 'acc':
        _i += 1
        acc += _value
    elif _name == 'nop':
        _i += 1
    elif _name == 'jmp':
        _i = max(0, _i + _value)
    return [acc, _i]


def is_leads_to_infiniti_loop(_num, arr, executed):
    _executed = executed[::-1]
    _executed = _executed[0:_executed.index(_num)]
    # count of instructions to check ahead in future
    ahead_check = 100
    _i = _num
    _inst = arr[_num]
    _inst = _inst.replace('jmp', 'nop') if _inst.__contains__(
        'jmp') else _inst.replace('nop', 'jmp')
    while ahead_check > -1:
        print(f'executed {_inst}')
        if _i in _executed:
            print(f'{_num} {arr[_num]} infinite')
            return True
        [_, _i] = executor(_inst, _i, 0)
        if _i >= len(arr):
            return False
        _inst = arr[_i]
        ahead_check -= 1

    return False


def parts(arr, partTwo=True):
    acc = 0
    _executed = []
    _map = {}
    _i = 0
    while True:
        if _i in _executed:
            if not partTwo:
                break
            _executed.reverse()
            print(_executed)
            found = False
            for _y in _executed:
                _n = arr[_y][0:3]
                if _n == 'nop':
                    if not is_leads_to_infiniti_loop(_y, arr, _executed):
                        arr[_y] = arr[_y].replace('nop', 'jmp')
                        found = True
                        break
                elif _n == 'jmp':
                    if not is_leads_to_infiniti_loop(_y, arr, _executed):
                        arr[_y] = arr[_y].replace('jmp', 'nop')
                        found = True
                        break
            if found:
                print(f"found : {_y} : {arr[_y]}")
                parts(arr, False)
                exit()
        if _i >= len(arr):
            print('end')
            break

        instruction = arr[_i]
        _executed.append(_i)
        [acc, _i] = executor(instruction, _i, acc)
        _map[_i] = acc

    # print(f'partOne: {acc}')
    print(f'partTwo: {acc}')


inputs = [x.strip() for x in open('inputs.txt', 'r').readlines()]
parts(inputs)
