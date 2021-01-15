import sys
import os
f = open('03_C - Step.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
rst = 0
for i in range(1, N):
    if ls[i - 1] > ls[i]:
        rst += ls[i - 1] - ls[i]
        ls[i] += ls[i - 1] - ls[i]
print(rst)
