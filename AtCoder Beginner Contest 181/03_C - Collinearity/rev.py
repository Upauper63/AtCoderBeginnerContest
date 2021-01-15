import os
import sys
f = open('03_C - Collinearity.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
ls = []
for i in range(N):
    ls.append(list(map(int, input().split(' '))))
combis = itertools.combinations(range(N), 3)
for combi in combis:
    dx1, dy1 = ls[combi[1]][0] - ls[combi[0]][0], ls[combi[1]][1] - ls[combi[0]][1]
    dx2, dy2 = ls[combi[2]][0] - ls[combi[0]][0], ls[combi[2]][1] - ls[combi[0]][1]
    if dx1 * dy2 == dx2 * dy1:
        print('Yes')
        exit()
print('No')