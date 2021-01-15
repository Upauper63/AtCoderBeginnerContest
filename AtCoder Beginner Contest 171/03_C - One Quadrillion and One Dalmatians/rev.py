import os
import sys
f = open('03_C - One Quadrillion and One Dalmatians.txt', 'r')
sys.stdin = f

N = int(input()) - 1
ans = ''
for i in range(1, 15):
    if N >= 26 ** i:
        N -= 26 ** i
        continue
    for j in range(i):
        d = N % 26
        ans += chr(d + ord('a'))
        N //= 26
    print(ans[::-1])
    exit()