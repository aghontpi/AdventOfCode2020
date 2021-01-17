#! /usr/bin/python3
from copy import deepcopy

valid_messages = {}


def partOne(rule_idx):
    # generata all the possible cobinations
    # loop through all the message to find valid messages
    rule_value = rules_map[rule_idx]
    if 'a' in rule_value or 'b' in rule_value:
        return rule_value
    if rule_idx in valid_messages:
        return valid_messages[rule_idx]
    message_acc = []
    for rules_list in rule_value:
        result = []
        for rule_item in rules_list:
            tmp = partOne(rule_item)
            if len(result) == 0:
                result = deepcopy(tmp)
            else:
                rules_or = []
                for _y in tmp:
                    for _z in result:
                        rules_or.append(_z+_y)
                result = deepcopy(rules_or)
        message_acc += result
    valid_messages[rule_idx] = message_acc
    return message_acc


inputs = open('input.txt', 'r').read()
[rules, messages] = inputs.split("\n\n")
rules = rules.split('\n')
messages = messages.split("\n")
rules_map = {}
for line in rules:
    [index, rule_content] = line.split(": ")
    index = int(index)
    if rule_content.__contains__('|'):
        rule_content = rule_content.split("|")
        t = []
        for _rule_item in rule_content:
            _rule_item = _rule_item.strip()
            t.append(list(map(lambda x: int(
                x.strip()), _rule_item.split(' '))))
        rules_map[index] = t
    elif rule_content.__contains__('"'):
        rule_content = rule_content.replace('"', '')
        rules_map[index] = [rule_content]
    else:
        rule_content = map(lambda x: int(x.strip()), rule_content.split(' '))
        rule_content = list(rule_content)
        rules_map[index] = [rule_content]

valid_generated_messages = partOne(0)
valid_message_map = set()
for x in valid_generated_messages:
    valid_message_map.add(x)
count = 0
for message in messages:
    if message in valid_message_map:
        count += 1
print(f'PartOne: {count}')

rules_map_2 = deepcopy(rules_map)

rules_map_2[8] = [[42], [42, 8]]
rules_map_2[11] = [(42, 31), [42, 11, 31]]


def partTwo(msg, _rule=0, pos=0):
    global rules_map_2
    if pos == len(msg):
        return []

    rules = rules_map_2[_rule]

    # building msg up
    if 'a' in rules or 'b' in rules:
        if msg[pos] == rules[0]:
            return [pos + 1]
        return []

    rules_match = []
    for rule in rules:
        rules_sub_matches = [pos]

        for or_rule in rule:
            tmp = []
            for _pos in rules_sub_matches:
                tmp.extend(partTwo(msg, or_rule, _pos))
            rules_sub_matches = tmp

        rules_match += rules_sub_matches

    return rules_match


_count = 0
for message in messages:
    if len(message) in partTwo(message):
        _count += 1

print(f'PartTwo:{_count}')
