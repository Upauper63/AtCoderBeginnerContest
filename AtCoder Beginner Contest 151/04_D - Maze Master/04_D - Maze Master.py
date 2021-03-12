
import sys
f = open('04_D - Maze Master.txt', 'r')
sys.stdin = f

import collections
H, W = map(int, input().split(' '))
ls = []
for _ in range(H):
    ls.append(list(input()))
def search(start, T, ls):
    val = 0
    S = collections.deque([start])
    while S:
        y, x = S.popleft()
        for pos in [[y, x + 1], [y + 1, x], [y, x - 1], [y - 1, x]]:
            tmp_y, tmp_x = pos
            if tmp_y < 0 or tmp_x < 0 or tmp_y >= H or tmp_x >= W or pos == start:
                continue
            if ls[tmp_y][tmp_x] == '.' and T[tmp_y][tmp_x] == 0:
                T[tmp_y][tmp_x] = T[y][x] + 1
                val = max(val, T[y][x] + 1)
                S.append(pos)
    return val
rst = 0
for i in range(H):
    for j in range(W):
        if ls[i][j] == '#':
            continue
        val = search([i, j], [[0 for i in range(W)] for j in range(H)], ls)
        rst = max(val, rst)
print(rst)