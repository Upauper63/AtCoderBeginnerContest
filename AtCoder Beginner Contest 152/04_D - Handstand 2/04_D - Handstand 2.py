import os
import sys
f = open('04_D - Handstand 2.txt', 'r')
sys.stdin = f

N = int(input())
cnt_ls = [[0 for i in range(10)] for j in range(10)]
for i in range(1, N + 1):
    btm = i % 10
    top = int(str(i)[:1])
    cnt_ls[top][btm] += 1
rst = 0
for i in range(1, 10):
    for j in range(1, 10):
        rst += cnt_ls[i][j] * cnt_ls[j][i]
print(rst)