import os
import sys
f = open('03_C - Skill Up.txt', 'r')
sys.stdin = f

import itertools
N, M, X = map(int, input().split(' '))
books = [ [] for i in range(N) ]
for i in range(N):
    tmp = list(map(int, input().split(' ')))
    books[i] = {'price': tmp[0], 'exp': tmp[1:]}

perms = itertools.permutations(range(N))
rst = float('inf')
for perm in perms:
    price = 0
    exp = [ 0 for i in range(M) ]
    for idx in perm:
        price += books[idx]['price']
        is_end = True
        for s in range(M):
            exp[s] += books[idx]['exp'][s]
            if exp[s] < X:
                is_end = False
        if is_end:
            rst = min(rst, price)
            break
if rst == float('inf'):
    print(-1)
else:
    print(rst)