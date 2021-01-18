import os
import sys
f = open('04_D - Alter Altar.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(input())
sorted_ls = sorted(ls)
rst = 0
for i, j in zip(ls, sorted_ls):
    if j == 'W':
        break
    elif i != j:
        rst += 1
print(rst)