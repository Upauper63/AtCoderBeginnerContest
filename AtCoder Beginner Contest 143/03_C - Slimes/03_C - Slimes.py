import sys
import os
f = open('03_C - Slimes.txt', 'r')
sys.stdin = f

rst = []
N = int(input())
S = input()
tmp_val = ''
for i in S:
    if tmp_val != i:
        rst.append(i)
        tmp_val = i
print(len(rst))