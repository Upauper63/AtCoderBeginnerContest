import sys
f = open('04_D - Lamp.txt', 'r')
sys.stdin = f

import bisect
h, w = map(int, input().split(' '))
ls = []
v_wall = [[-1, h] for _ in range(w)]
h_wall = [[-1, w] for _ in range(h)]
for i in range(h):
    val = list(input())
    for j in range(w):
        if val[j] == '#':
            v_wall[j].append(i)
            h_wall[i].append(j)
    h_wall[i].sort()
    ls.append(val)
for j in range(w):
    v_wall[j].sort()
rst = 0
for i, val in enumerate(ls):
    for j, v in enumerate(val):
        if v == '.':
            h_wall_idx = bisect.bisect(h_wall[i], j)
            v_wall_idx = bisect.bisect(v_wall[j], i)
            if h_wall[i][h_wall_idx - 1] == -1:
                h_val = h_wall[i][h_wall_idx]
            else:
                h_val = h_wall[i][h_wall_idx] - h_wall[i][h_wall_idx - 1] - 1
            if v_wall[j][v_wall_idx - 1] == -1:
                v_val = v_wall[j][v_wall_idx]
            else:
                v_val = v_wall[j][v_wall_idx] - v_wall[j][v_wall_idx - 1] - 1
            tmp = h_val + v_val - 1
            rst = max(tmp, rst)
print(rst)
