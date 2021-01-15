import sys
import os
f = open('03_C - Tax Increase.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
for i in range(1, 13000):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        print(i)
        break
else:
    print(-1)