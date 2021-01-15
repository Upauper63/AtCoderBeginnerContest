import os
import sys
f = open('03_C - Green Bin.txt', 'r')
sys.stdin = f

import collections
N = int(input())
ls = []
for i in range(N):
    s = list(input())
    s.sort()
    ls.append(''.join(s))
cnt_ls = collections.Counter(ls)
rst = 0
for i in cnt_ls.values():
    rst += i * (i - 1) // 2
print(rst)