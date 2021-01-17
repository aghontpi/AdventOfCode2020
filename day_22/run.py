#! /usr/bin/python3
from collections import deque
from copy import deepcopy

inputs = open('input.txt', 'r').read()
p1, p2 = inputs.split('\n\n')
p1 = p1.split("\n")
p2 = p2.split("\n")

player_1 = deque()
player_2 = deque()

p1.pop(0)
while p1:
    value = p1.pop(0)
    player_1.append(int(value))

p2.pop(0)
while p2:
    value = p2.pop(0)
    player_2.append(int(value))


def partOne(player_1, player_2):
    while player_1 and player_2:
        player_1_card = player_1.popleft()
        player_2_card = player_2.popleft()
        print(f'player 1 deck: {player_1}')
        print(f'player 2 deck: {player_2}')
        print(f'player 1 plays: {player_1_card}')
        print(f'player 2 plays: {player_2_card}')
        if player_1_card > player_2_card:
            print(f'player 1 wins')
            player_1.append(player_1_card)
            player_1.append(player_2_card)
        elif player_1_card < player_2_card:
            print('f"player 2 wins')
            player_2.append(player_2_card)
            player_2.append(player_1_card)
    print(f"post game: \nplayer1:{player_1}\nplayer2:{player_2}")
    winner = max(player_1, player_2)
    winner.reverse()
    _sum = 0
    for value, index in enumerate(winner, 1):
        _sum = _sum + (value * index)
    print('partOne: ', _sum)


partOne(deepcopy(player_1), deepcopy(player_2))


def partTwo(player_1, player_2, hash_set, _round, _game):
    def create_new_deck(player_deck_copy, _value):
        player_1_new_deck = deque()
        # ignore current element
        while _value and player_deck_copy:
            player_1_new_deck.append(player_deck_copy.popleft())
            _value = _value - 1
        return player_1_new_deck

    while True:
        print(f'-- Round {_round} (Game {_game}) --')
        if not player_1:
            return (player_2, 2)
        if not player_2:
            return (player_1, 1)

        _set = (tuple(player_1), tuple(player_2))
        if _set in hash_set:
            return (player_1, 1)
        else:
            hash_set.add(_set)
        player_1_value = player_1.popleft()
        player_2_value = player_2.popleft()
        print(f'player 1 deck: {player_1}')
        print(f'player 2 deck: {player_2}')
        print(f'player 1 plays: {player_1_value}')
        print(f'player 2 plays: {player_2_value}')
        if player_1_value <= player_1.__len__() and player_2_value <= player_2.__len__():
            player_1_new_deck = create_new_deck(
                deepcopy(player_1), player_1_value)
            player_2_new_deck = create_new_deck(
                deepcopy(player_2), player_2_value)
            print('creating sub game')
            _, player = partTwo(
                player_1_new_deck, player_2_new_deck, set(), 1, _game+1)
            if player == 1:
                print("player 1 wins")
                player_1.append(player_1_value)
                player_1.append(player_2_value)
            else:
                print('player 2 wins')
                player_2.append(player_2_value)
                player_2.append(player_1_value)
        elif player_1_value > player_2_value:
            print(f'player 1 wins')
            player_1.append(player_1_value)
            player_1.append(player_2_value)
        elif player_1_value < player_2_value:
            print(f'player 2 wins')
            player_2.append(player_2_value)
            player_2.append(player_1_value)
        _round += 1


_winner, player = partTwo(deepcopy(player_1), deepcopy(player_2), set(), 1, 1)
print('post game results')
print(_winner, f'winning player: {player}')
_winner.reverse()
_sum = 0
for value, index in enumerate(_winner, 1):
    _sum = _sum + (value * index)
print(f'partTwo: {_sum}')
