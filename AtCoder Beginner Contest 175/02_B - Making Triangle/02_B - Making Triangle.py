import os
import sys
f = open('02_B - Making Triangle.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
ls = list(map(int, input().split(' ')))
comb = itertools.combinations(range(N), 3)
rst = 0
var = []
for i in comb:
    tmp = [ []  for x in range(3)]
    for j in range(3):
        tmp[j] = ls[i[j]]
    tmp.sort()
    if tmp[0] + tmp[1] > tmp[2] and tmp[0] != tmp[1] and tmp[1] != tmp[2]:
        rst += 1
print(rst)