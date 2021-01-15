import os
import sys
f = open('03_C - Travel.txt', 'r')
sys.stdin = f

import itertools
N, K = map(int, input().split(' '))
ls = []
for i in range(N):
    ls.append(list(map(int, input().split(' '))))
var = itertools.permutations(range(1, N))
rst = 0
for pat in var:
    cnt = 0
    cnt += ls[0][pat[0]]
    for i in range(N - 2):
        cnt += ls[pat[i]][pat[i + 1]]
    cnt += ls[pat[-1]][0]
    if cnt == K:
        rst += 1
print(rst)