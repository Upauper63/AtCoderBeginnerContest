import sys
f = open('03_C - Tour.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split(' '))
edges = [[] for _ in range(n)]
is_reached = [False for _ in range(n)]
rst = 0
for _ in range(m):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    edges[a].append(b)

def dfs(x):
    if is_reached[x]:
        return
    is_reached[x] = True
    for edge in edges[x]:
        dfs(edge)

for i in range(n):
    is_reached = [False for _ in range(n)]
    is_reached[i] = True
    for edge in edges[i]:
        dfs(edge)
    rst += sum(is_reached)

print(rst)