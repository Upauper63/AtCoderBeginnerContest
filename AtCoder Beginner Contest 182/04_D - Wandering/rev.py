import os
import sys
f = open('04_D - Wandering.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
sum_ls = []
sum_ls[0] = 0
max_ls = []
max_ls[0] = 0
for i in range(len(ls) - 1):
    sum_ls[i + 1].append(sum_ls[i] + ls[i])
print(sum_ls)