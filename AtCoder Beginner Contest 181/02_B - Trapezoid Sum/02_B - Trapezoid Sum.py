import os
import sys
f = open('02.txt', 'r')
sys.stdin = f

N = int(input())
rst = 0
for i in range(N):
    a, b = map(int, input().split(' '))
    rst += (a + b) * (b - a + 1) // 2
print(rst)