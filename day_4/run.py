#! /usr/bin/python3
import json
import re


def validateData(key, value):
    valid = True

    def dataValidator(lt, gt):
        intValue = int(value)
        return len(value) == 4 and (intValue >= lt and intValue <= gt)

    if key == 'byr':
        if not dataValidator(1920, 2002):
            valid = False
    elif key == 'iyr':
        if not dataValidator(2010, 2020):
            valid = False
    elif key == 'eyr':
        if not dataValidator(2020, 2030):
            valid = False
    elif key == 'hgt':
        if value.endswith('cm'):
            indexc = value.index('c')
            value = value[0: indexc]
            value = int(value)
            if not (value >= 150 and value <= 193):
                valid = False
        elif value.endswith('in'):
            indexi = value.index('i')
            value = value[0:indexi]
            value = int(value)
            if not (value >= 59 and value <= 76):
                valid = False
        else:
            valid = False
    elif key == 'hcl':
        if not re.match('^#[0-9a-f]{6}$', value):
            valid = False
    elif key == 'ecl':
        if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False
    elif key == 'pid':
        if not re.match('^[0-9]{9}$', value):
            valid = False
    return valid


def parts(part, arr):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid = 0
    for x in arr:
        x = x.strip().split()
        tmp = fields[:]
        if x:
            for xkeyvalue in x:
                key, value = xkeyvalue.split(':')
                if part == 'one' or (part == 'two' and validateData(key, value)):
                    tmp.pop(tmp.index(key))
            if 'cid' in tmp:
                tmp.pop(tmp.index('cid'))
            if(len(tmp) == 0):
                valid += 1
            # print(tmp, x)
    return valid


inputs = open('inputs.txt', 'r').read().split('\n\n')
print('partOne', parts('one', inputs))
print('partTwo', parts('two', inputs))
