import sys
import os
f = open('03_C - management.txt', 'r')
sys.stdin = f

N = int(input())
A_ls = list(map(int, input().split(' ')))
ls = [0] * N
for i in A_ls:
    ls[i - 1] += 1
for i in ls:
    print(i)