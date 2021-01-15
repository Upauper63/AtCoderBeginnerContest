import sys
import os
f = open('03_C - Traveling Salesman around Lake.txt', 'r')
sys.stdin = f

K, N = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
max_dist = 0
for i in range(N):
    nxt = (i + 1 ) % N
    dist = A_ls[nxt] - A_ls[i]
    if dist < 0:
        dist += K
    max_dist = max(max_dist, dist)
print(K - max_dist)