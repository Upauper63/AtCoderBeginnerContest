import os
import sys
f = open('03_C - Slimes.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(input())
tmp = ''
cnt = 0
for i in ls:
    if not i == tmp:
        cnt += 1
        tmp = i
print(cnt)