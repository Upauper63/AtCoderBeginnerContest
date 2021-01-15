import os
import sys
f = open('03_C - City Savers.txt', 'r')
sys.stdin = f

N = int(input())
A_ls = list(map(int, input().split(' ')))
B_ls = list(map(int, input().split(' ')))
cnt = 0
for i in range(N):
    if A_ls[i] + A_ls[i + 1] <= B_ls[i]:
        cnt += A_ls[i] + A_ls[i + 1]
        A_ls[i + 1] = 0
    elif A_ls[i] <= B_ls[i]:
        A_ls[i + 1] -= B_ls[i] - A_ls[i]
        cnt += B_ls[i]
    else:
        cnt += B_ls[i]
print(cnt)