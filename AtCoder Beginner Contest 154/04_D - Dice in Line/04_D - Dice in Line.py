import os
import sys
f = open('04_D - Dice in Line.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
val_ls = [[] for i in range(N)]
val_ls[0] = (1 + ls[0]) / 2
for i in range(N - 1):
    val_ls[i + 1] = val_ls[i] + (1 + ls[i + 1]) / 2
rst = val_ls[K - 1]
for i in range(K, N):
    rst = max(val_ls[i] - val_ls[i - K], rst)
print(rst)