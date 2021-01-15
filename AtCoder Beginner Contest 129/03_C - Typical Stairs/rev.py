import os
import sys
f = open('03_C - Typical Stairs.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
ls = [1] + [ 0 for i in range(N) ]
ls[1] = 1
for i in range(M):
    a = int(input())
    if a == 1:
        ls[a] = 0
    else:
        ls[a] = -1
for i in range(N - 1):
    if ls[i + 2] == -1:
        ls[i + 2] = 0
    else:
        ls[i + 2] = ls[i] + ls[i + 1]
print(ls[N] % 1000000007)