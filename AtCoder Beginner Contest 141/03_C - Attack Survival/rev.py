import os
import sys
f = open('03_C - Attack Survival.txt', 'r')
sys.stdin = f

N, K, Q = map(int, input().split(' '))
ls = [ K for i in range(N) ]
for i in range(Q):
    tmp = int(input()) - 1
    ls[tmp] += 1
for i in ls:
    if i - Q > 0:
        print('Yes')
    else:
        print('No')