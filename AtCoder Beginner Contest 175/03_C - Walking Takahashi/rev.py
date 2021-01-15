import os
import sys
f = open('03_C - Walking Takahashi.txt', 'r')
sys.stdin = f

X, K, D = map(int, input().split(' '))
X = abs(X)
if K * D <= X:
    print(abs(X - K * D))
else:
    K -= X // D
    X -= D * (X // D)
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))