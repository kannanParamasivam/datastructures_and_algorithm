# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, T):

    s1 = convert_to_string(S)
    s2 = convert_to_string(T)

    if len(s1) != len(s2):
        return False
    
    for i, c in enumerate(s1):
        
        if c != '?' and s2[i] != '?' and c != s2[i]:
            return False
    
    return True


def convert_to_string(val):

    res = []

    for c in val:
        if c.isalpha():
            res.append(c)
        else:
            v = ['?'] * int(c)
            res.extend(v)

    return res


print(solution('10a', 'a10'))

'''
1. check length
2. check mutually available characters are equal (including case)

eg 1
A2Le - 2pL1
A2Le - 3L1

A ? ? L e
? ? p L ?

eg 2
ba1 - 1Ad

b a ?
? A d

'''

'''
A2Le

[A,] [?]*n
'''
