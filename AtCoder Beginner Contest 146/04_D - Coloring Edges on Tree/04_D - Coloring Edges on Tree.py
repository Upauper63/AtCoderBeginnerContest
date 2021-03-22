import sys
f = open('04_D - Coloring Edges on Tree.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(200000)
n = int(input())
edges = [[] for _ in range(n)]
n -= 1
input_ls = []
def int_minusone(x):
    return int(x) - 1
for i in range(n):
    a, b = map(int_minusone, input().split(' '))
    edges[a].append(b)
    input_ls.append((a, b))
colors = {}
color_num = 0
def dfs(x, banned_color):
    global color_num
    color = 1
    if len(edges[x]) == 0:
        return
    for edge in edges[x]:
        if banned_color == color:
            color += 1
        colors[(x, edge)] = color
        color_num = max(color, color_num)
        dfs(edge, color)
        color += 1
    
dfs(0, 0)

print(color_num)
for (a, b) in input_ls:
    print(colors[(a, b)])
