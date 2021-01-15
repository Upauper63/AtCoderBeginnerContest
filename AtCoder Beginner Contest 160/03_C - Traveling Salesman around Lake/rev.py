import sys
import os
f = open('03_C - Traveling Salesman around Lake.txt', 'r')
sys.stdin = f

K, N = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
long_dist = 0
for i in range(N):
    if i == (N - 1):
        l =  K - ls[i] + ls[0]
    else:
        l = ls[i + 1] - ls[i]
    long_dist = max(long_dist, l)
print(K - long_dist)