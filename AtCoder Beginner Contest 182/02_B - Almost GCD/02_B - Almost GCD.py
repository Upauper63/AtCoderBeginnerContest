import os
import sys
f = open('02.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
max_cnt, rst = 0, 0
for i in range(2, max(ls) + 1):
    cnt = 0
    for j in ls:
        if j % i == 0:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    if max_cnt == cnt:
        rst = i
print(rst)