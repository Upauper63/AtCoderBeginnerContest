
import sys
f = open('03.txt', 'r')
sys.stdin = f

import itertools
N, K = map(int, input().split(' '))
ls = [ [] for i in range(N) ]
for i in range(N):
    ls[i] = list(map(int, input().split(' ')))

perms = itertools.permutations(range(1, N))
rst = 0
for perm in perms:
    val = 0
    val += ls[0][perm[0]]
    for i in range(0, N - 2):
        val += ls[perm[i]][perm[i + 1]]
    val += ls[perm[-1]][0]
    if val == K:
        rst += 1
print(rst)