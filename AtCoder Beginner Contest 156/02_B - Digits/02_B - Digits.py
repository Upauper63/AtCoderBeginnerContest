import sys
import os
f = open('02_B - Digits.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))

cnt = 0
while N:
    N //= K
    cnt += 1
print(cnt)