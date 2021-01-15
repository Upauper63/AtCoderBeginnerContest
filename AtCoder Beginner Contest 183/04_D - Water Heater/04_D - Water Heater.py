import os
import sys
f = open('04_D - Water Heater.txt', 'r')
sys.stdin = f

N, W = map(int, input().split(' '))
ls = [ 0 for i in range(2 * 10 ** 6 + 1) ]
for i in range(N):
    s, t, p = map(int, input().split(' '))
    ls[s] += p
    ls[t] -= p
for i in range(2 * 10 ** 6):
    ls[i + 1] += ls[i]
if max(ls) > W:
    print('No')
else:
    print('Yes')