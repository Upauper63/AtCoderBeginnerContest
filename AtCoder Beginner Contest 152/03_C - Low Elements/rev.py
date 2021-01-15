import os
import sys
f = open('03_C - Low Elements.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
tmp_min = float('inf')
rst = 0
for i in ls:
    if i <= tmp_min:
        tmp_min = i
        rst += 1
print(rst)