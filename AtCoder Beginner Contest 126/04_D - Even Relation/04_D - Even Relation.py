import sys
f = open('04_D - Even Relation.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split(' '))
    w %= 2
    edges[u - 1].append({v - 1: w})
    edges[v - 1].append({u - 1: w})
res = [0] * n

def dfs(prev, edge, dist):
    if dist % 2:
        res[edge] = 1
    for val in edges[edge]:
        for k, v in val.items():
            if k == prev:
                continue
            dfs(edge, k, dist + v)
dfs(-1, 0, 0)
for r in res:
    print(r)