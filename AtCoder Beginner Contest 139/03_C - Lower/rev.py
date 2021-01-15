import os
import sys
f = open('03_C - Lower.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' '))) + [float('inf')]
cnt, rst = 0, 0
for i in range(N):
    if ls[i] >= ls[i + 1]:
        cnt += 1
    else:
        if cnt > rst:
            rst = cnt
        cnt = 0
print(rst)