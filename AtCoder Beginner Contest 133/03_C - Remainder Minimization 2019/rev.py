import os
import sys
f = open('03_C - Remainder Minimization 2019.txt', 'r')
sys.stdin = f

L, R = map(int, input().split(' '))
if R >= L + 2018:
    print(0)
    exit()
if L >= 2019:
    L %= 2019
    R %= 2019
rst = float('inf')
for i in range(L, R):
    for j in range(L + 1, R + 1):
        rst = min(rst, (i * j) % 2019)
print(rst)