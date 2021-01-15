import os
import sys
f = open('03_C - Count Order.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))
perms = itertools.permutations(range(1, N + 1))
for idx, perm in enumerate(perms):
    if P == perm:
        a = idx + 1
    if Q == perm:
        b = idx + 1
print(abs(a - b))