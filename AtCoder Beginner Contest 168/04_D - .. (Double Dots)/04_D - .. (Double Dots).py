from collections import deque
import os
import sys
f = open('04_D - .. (Double Dots).txt', 'r')
sys.stdin = f

import collections
N, M = map(int, input().split(' '))
graph = [[] for i in range(N + 1)]
dist = [-1 for i in range(N + 1)]
dist[0], dist[1] = 0, 0
pre = [0 for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
deq = collections.deque()
deq.append(1)
while deq:
    i = deq.popleft()
    for j in graph[i]:
        if dist[j] != -1:
            continue
        dist[j] = dist[i] + 1
        pre[j] = i
        deq.append(j)
if -1 in dist:
    print('No')
else:
    print('Yes')
    for i in pre[2:]:
        print(i)