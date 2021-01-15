import sys
import os
f = open('02_B - Roller Coaster.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
h_ls = map(int, input().split(' '))
cnt = 0
for i in h_ls:
    if i >= K:
        cnt += 1
print(cnt)