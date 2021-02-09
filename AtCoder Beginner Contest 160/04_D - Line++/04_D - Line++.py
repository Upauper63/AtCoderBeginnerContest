import os
import sys
f = open('04_D - Line++.txt', 'r')
sys.stdin = f

N, X, Y = map(int, input().split(' '))
cnt_ls = [0 for i in range(N - 1)]
for i in range(1, N):
    for j in range(i + 1, N + 1):
        dist = min(j - i, abs(i - X) + abs(j - Y) + 1)
        cnt_ls[dist - 1] += 1
for i in cnt_ls:
    print(i)