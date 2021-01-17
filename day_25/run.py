#! /usr/bin/python3

tmp = open('input.txt', 'r').read().split('\n')
inputs = []
for _input in tmp:
    inputs.append(int(_input))

assert(len(inputs) == 2)
cards_public_key, doors_public_key = inputs

card_secret = None
encryption_key = None
prime = 7

_count = 0
tmp = 1
while not card_secret:
    if tmp == cards_public_key:
        card_secret = tmp
        break
    tmp = tmp * prime
    tmp = tmp % 20201227
    _count += 1
tmp = 1
while _count > 0:
    tmp = tmp * doors_public_key
    tmp = tmp % 20201227
    _count -= 1

encryption_key = tmp

print(encryption_key)
