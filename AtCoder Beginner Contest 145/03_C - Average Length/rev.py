import os
import sys
f = open('03_C - Average Length.txt', 'r')
sys.stdin = f

import itertools, math
N = int(input())
ls = []
for i in range(N):
    ls.append(tuple(map(int, input().split(' '))))
perms = itertools.permutations(range(N))
val = 0
for perm in perms:
    for i in range(N - 1):
        val += math.sqrt((ls[perm[i + 1]][0] - ls[perm[i]][0]) ** 2 + (ls[perm[i + 1]][1] - ls[perm[i]][1]) ** 2)
print(val / math.factorial(N))