import sys
import os
f = open('03_C - Peaks.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
H_ls = list(map(int, input().split(' ')))
edge = [ [] for i in range(N)]
cnt = 0
for i in range(M):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
for i in range(N):
    is_peak = True
    for neighbor in edge[i]:
        if H_ls[i] <= H_ls[neighbor]:
            is_peak = False
            break
    if is_peak:
        cnt += 1
print(cnt)
