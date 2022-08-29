import sys
f = open('B - Triangle (Easier).txt', 'r')
sys.stdin = f

n, m = map(int, input().split(' '))
edges = [[] for i in range(n)]
rst = 0
for i in range(m):
    u, v = map(int, input().split(' '))
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)

def check(i, edge, p):
    tmp_val = 0
    if p == 1:
        if edge in edges[i]:
            return 1
        else:
            return 0
    for tmp_edge in edges[edge]:
        if tmp_edge <= edge:
            continue
        tmp_val += check(i, tmp_edge, p + 1)
    return tmp_val

for i in range(n):
    for edge in edges[i]:
        if edge > i:
            rst += check(i, edge, 0)
print(rst)