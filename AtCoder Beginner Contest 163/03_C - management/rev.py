import os
import sys
f = open('03_C - management.txt', 'r')
sys.stdin = f

N = int(input())
rst = [ 0 for i in range(N)]
ls = list(map(int, input().split(' ')))
for i in ls:
    rst[i - 1] += 1
[ print(i) for i in rst ]