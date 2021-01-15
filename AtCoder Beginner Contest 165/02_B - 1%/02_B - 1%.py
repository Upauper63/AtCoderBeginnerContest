import sys
import os
f = open('02_B - 1%.txt', 'r')
sys.stdin = f

A = 100
X = int(input())
cnt = 0

while X > A:
    cnt += 1
    A += A // 100
print(cnt)