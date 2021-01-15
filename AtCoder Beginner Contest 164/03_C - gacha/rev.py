import os
import sys
f = open('03_C - gacha.txt', 'r')
sys.stdin = f

N = int(input())
rst = set()
for i in range(N):
    rst.add(input())
print(len(rst))