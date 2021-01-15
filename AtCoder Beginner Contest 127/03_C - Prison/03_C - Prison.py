import os
import sys
f = open('03_C - Prison.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
min_val = 0
max_val = float('inf')

for i in range(M):
    L, R = map(int, input().split(' '))
    if R < min_val or max_val < L:
        print(0)
        exit()
    min_val = max(min_val, L)
    max_val = min(max_val, R)
print(max_val - min_val + 1)