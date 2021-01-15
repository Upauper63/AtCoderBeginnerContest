import os
import sys
f = open('03_C - Build Stairs.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
ls.reverse()
for i in range(N - 1):
    if ls[i + 1] > ls[i]:
        ls[i + 1] -= 1
if ls == sorted(ls, reverse=True):
    print('Yes')
else:
    print('No')