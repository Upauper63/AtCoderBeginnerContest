import os
import sys
f = open('03_C - Tax Increase.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
rst = min(A / 0.08, B / 0.1)
while int(rst * 0.08) == A or int(rst * 0.1) == B:
    if int(rst * 0.08) == A and int(rst * 0.1) == B:
        print(int(rst))
        exit()
    rst += 1
print(-1)