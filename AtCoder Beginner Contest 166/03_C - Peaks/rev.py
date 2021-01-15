import os
import sys
f = open('03_C - Peaks.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
edges = [ [] for i in range(N) ]
cnt = 0
for i in range(M):
    a, b = map(int, input().split(' '))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
for idx, edge in enumerate(edges):
    is_good = True
    for i in edge:
        if ls[i] >= ls[idx]:
            is_good = False
            break
    if is_good:
        cnt += 1
print(cnt)