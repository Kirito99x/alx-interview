#!/usr/bin/python3
'''minimum number of operations needed to result in n H characters.'''


def minOperations(n):
    '''find the minimum numbers of operations needed to result in n H characters.'''
    if not isinstance(n, int):
        return 0
    num_ops = 0
    cp_pa = 0
    Done = 1
    while Done < n:
        if cp_pa == 0:
            cp_pa = Done
            Done += cp_pa
            num_ops += 2
        elif n - Done > 0 and (n - Done) % Done == 0:
            cp_pa = Done
            Done += cp_pa
            num_ops += 2
        elif cp_pa > 0:
            Done += cp_pa
            num_ops += 1
    return num_ops
