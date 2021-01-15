import sys
import os
f = open('02_B - Bite Eating.txt', 'r')
sys.stdin = f

N, L = map(int, input().split(' '))
ls = [i + L for i in range(N)]
if 0 in ls:
    print(sum(ls))
elif sum(ls) < 0:
    print(sum(ls) - max(ls))
else:
    print(sum(ls) - min(ls))