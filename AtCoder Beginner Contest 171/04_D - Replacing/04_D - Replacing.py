import os
import sys
f = open('04_D - Replacing.txt', 'r')
sys.stdin = f

import collections
N = int(input())
ls = list(map(int, input().split(' ')))
dic = collections.Counter(ls)
Q = int(input())
rst = sum(ls)
for i in range(Q):
    b, c = map(int, input().split(' '))
    cnt = dic[b]
    del dic[b]
    if c in dic:
        dic[c] += cnt
    else:
        dic[c] = cnt
    rst += (c - b) * cnt
    print(rst)