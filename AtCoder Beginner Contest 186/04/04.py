import os
import sys
f = open('04.txt', 'r')
sys.stdin = f

import itertools
N = int(input())
ls = list(map(int, input().split(' ')))
comb_ls = itertools.combinations(ls, 2)
rst = 0
for s, t in comb_ls:
    rst += abs(s - t)
print(rst)