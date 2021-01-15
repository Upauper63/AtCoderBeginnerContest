import os
import sys
f = open('03_C - Distinct or Not.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
rst = []
for i in ls:
    if i in rst:
        print('NO')
        exit()
    else:
        rst.append(i)
print('YES')