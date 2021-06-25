import sys
f = open('04_D - Gathering Children.txt', 'r')
sys.stdin = f

import math
s = list(input())
boundary_ls = [0]
tmp = s[0]
for k, v in enumerate(s[1:]):
    if v != tmp:
        boundary_ls.append(k + 1)
        tmp = v
boundary_ls.append(len(s))
tmp_boundary = 0
boundary_sets = []
for i in range(0, len(boundary_ls) - 2, 2):
    boundary_sets.append((boundary_ls[i + 1] - boundary_ls[i], boundary_ls[i + 2] - boundary_ls[i + 1]))
val_ls = []
for i, j in boundary_sets:
    val_ls.append(math.ceil(i / 2) + math.floor(j / 2))
    val_ls.append(math.floor(i / 2) + math.ceil(j / 2))
rst = [0] * len(s)
for k, v in enumerate(boundary_ls[1: -1: 2]):
    rst[v - 1] = val_ls[2 * k]
    rst[v] = val_ls[2 * k + 1]
for i in rst:
    print(i)