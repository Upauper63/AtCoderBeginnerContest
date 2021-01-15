import os
import sys
f = open('03_C - Switches.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
sw = [ [0 for j in range(N)] for i in range(M) ]

for i in range(M):
    tmp = list(map(int, input().split(' ')))
    for idx in tmp[1:]:
        sw[i][idx - 1] = 1

condi = list(map(int, input().split(' ')))
rst = 0
for i in range(1 << N):
    pat = []
    for j in range(N):
        if i >> j & 1:
            pat.append(j)
    is_ok = True
    for idx, val in enumerate(sw):
        cnt = 0
        for s in pat:
            if val[s] == 1:
                cnt += 1
        if cnt % 2 != condi[idx]:
            is_ok = False
            break
    if is_ok:
        rst += 1
print(rst)