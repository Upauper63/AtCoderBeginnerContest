import os
import sys
f = open('02.txt', 'r')
sys.stdin = f

N, X = map(int, input().split(' '))
S = list(input())
for i in S:
    if i == 'x' and X > 0:
        X -=1
    elif i == 'o':
        X += 1
print(X)
