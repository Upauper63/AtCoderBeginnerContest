import sys
import os
f = open('03_C - Tsundoku.txt', 'r')
sys.stdin = f

n, m, k = map(int, input().split(' '))
ans = 0

a_ls = [0] + list(map(int, input().split(' ')))
b_ls = [0] + list(map(int, input().split(' ')))

for i in range(1, n+1):
    a_ls[i] += a_ls[i-1]
for i in range(1, m+1):
    b_ls[i] += b_ls[i-1]

b_cnt = m
for a_cnt in range(0, n+1):
    if a_ls[a_cnt] > k:
        continue
    while a_ls[a_cnt] + b_ls[b_cnt] > k:
        b_cnt -= 1
    ans = max(ans, a_cnt + b_cnt)

print(ans)