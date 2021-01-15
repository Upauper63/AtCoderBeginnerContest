import os
import sys
f = open('03_C - Alchemist.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
rst = ls[0]
for i in ls[1:]:
    rst = (rst + i) / 2
print(rst)