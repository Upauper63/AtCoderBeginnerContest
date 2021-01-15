import sys
import os
f = open('02_B - 0 or 1 Swap.txt', 'r')
sys.stdin = f

N = int(input())
p_ls = list(map(int, input().split(' ')))
cnt = 0

for i in range(len(p_ls) - 1):
    min_idx = i
    for j in range(i + 1, len(p_ls)):
        if p_ls[min_idx] > p_ls[j]:
            min_idx = j
    if min_idx != i:
        p_ls[min_idx], p_ls[i] = p_ls[i], p_ls[min_idx]
        cnt += 1
if cnt > 1:
    print('NO')
else:
    print('YES')