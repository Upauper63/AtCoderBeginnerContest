import os
import sys
f = open('02.txt', 'r')
sys.stdin = f

H, W = map(int, input().split(' '))
ls = []
min_val = float('inf')
for i in range(H):
    tmp = list(map(int, input().split(' ')))
    ls.append(tmp)
    min_val = min(min_val, min(tmp))
rst = 0
for s in ls:
    for t in s:
        rst += t - min_val
print(rst)