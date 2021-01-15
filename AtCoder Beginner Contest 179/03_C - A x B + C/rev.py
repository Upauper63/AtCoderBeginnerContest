import os
import sys
f = open('03_C - A x B + C.txt', 'r')
sys.stdin = f

N = int(input())
rst = 0
for i in range(1, N):
    rst += (N - 1) // i
print(rst)