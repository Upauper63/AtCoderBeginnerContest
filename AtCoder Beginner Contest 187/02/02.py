
import sys
f = open('02.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
ls = []
rst = 0
for i in range(N):
    ls.append(list(map(int, input().split(' '))))
combis = itertools.combinations(range(N), 2)
for combi in combis:
    dx = ls[combi[0]][0] - ls[combi[1]][0]
    dy = ls[combi[0]][1] - ls[combi[1]][1]
    if -1 <= dy / dx <= 1:
        rst += 1
print(rst)