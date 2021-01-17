#! /usr/bin/python3

def is_palindrome(_str, _start, _end):
    # recursion should run untill start and end not the same,
    if _str[_start] != _str[_end]:
        return False
    if _start != _end:
        return is_palindrome(_str, _start + 1, _end - 1)

    return True


_str = 'madam'
res = is_palindrome(_str, 0, len(_str) - 1)
print(res)
