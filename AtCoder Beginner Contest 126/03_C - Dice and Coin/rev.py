import os
import sys
f = open('03_C - Dice and Coin.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
rst = 0
for i in range(1, N + 1):
    cnt = 0
    while i < K:
        i *= 2
        cnt += 1
    rst += 1 / N * (1 / 2) ** cnt
print(rst)