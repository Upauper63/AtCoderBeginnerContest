import sys
f = open('B - Light It Up.txt', 'r')
sys.stdin = f

import math
n, k = map(int, input().split(' '))
a_ls = list(map(int, input().split(' ')))
edges = []
dist = [float('inf') for i in range(n)]
for i in range(n):
    edges.append(list(map(int, input().split(' '))))
for idx, v in enumerate(edges):
    if idx + 1 in a_ls:
        dist[idx] = 0
        continue
    for a in a_ls:
        w = edges[a - 1]
        tmp = (v[0] - w[0]) ** 2 + (v[1] - w[1]) ** 2
        dist[idx] = min(tmp, dist[idx])
print(math.sqrt(max(dist)))