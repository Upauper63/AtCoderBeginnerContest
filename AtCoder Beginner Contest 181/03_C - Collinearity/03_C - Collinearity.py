import os
import sys
f = open('03.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
ls = []

for i in range(N):
    ls.append(list(map(int, input().split(' '))))

combi = itertools.combinations(range(N), 3)
for i in combi:
    val = [ls[i[0]], ls[i[1]], ls[i[2]]]
    val.sort(key=lambda x:(x[0], x[1]))

    dx1 = val[1][0] - val[0][0]
    dx2 = val[2][0] - val[0][0]
    dy1 = val[1][1] - val[0][1]
    dy2 = val[2][1] - val[0][1]
    if dx1 * dy2 == dx2 * dy1:
        print('Yes')
        exit()
print('No')