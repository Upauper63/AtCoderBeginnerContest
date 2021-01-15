import sys
import os
f = open('03_C - H and V.txt', 'r')
sys.stdin = f

H, W, K = map(int, input().split(' '))
ls = []

for i in range(H):
    ls.append(list(input()))

rst = 0
for i in range(1 << H):
    for s in range(1 << W):
        cnt = 0
        for j in range(H):
            if i>>j & 1:
                continue
            for t in range(W):
                if s>>t & 1:
                    continue
                if ls[j][t] == '#':
                    cnt += 1
        if cnt == K:
            rst += 1
print(rst)