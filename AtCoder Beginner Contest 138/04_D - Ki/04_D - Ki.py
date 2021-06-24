import sys
f = open('04_D - Ki.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)
n, q = map(int, input().split(' '))
val_ls = [0 for _ in range(n)]
edges = [[] for _ in range(n)]
def recur(from_idx, to_idx, val):
    if from_idx == to_idx:
        return
    val_ls[to_idx] += val
    val = val_ls[to_idx]
    for edge in edges[to_idx]:
        if from_idx == edge:
            continue
        recur(to_idx, edge, val)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)
for _ in range(q):
    idx, val = map(int, input().split(' '))
    idx -= 1
    val_ls[idx] += val
for edge in edges[0]:
    recur(0, edge, val_ls[0])
for val in val_ls:
    print(val)