import os
import sys
f = open('03_C - Rally.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
rst = float('inf')
for i in range(min(ls), max(ls) + 1):
    val = 0
    for s in ls:
        val += (s - i) ** 2
    rst = min(rst, val)
print(rst)