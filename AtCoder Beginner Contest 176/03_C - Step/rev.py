import os
import sys
f = open('03_C - Step.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
rst = 0
for i in range(N - 1):
    if ls[i + 1] < ls[i]:
        rst += ls[i] - ls[i + 1]
        ls[i + 1] += ls[i] - ls[i + 1]
print(rst)