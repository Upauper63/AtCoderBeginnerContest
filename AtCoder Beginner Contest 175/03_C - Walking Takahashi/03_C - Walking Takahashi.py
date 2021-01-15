import os
import sys
f = open('03_C - Walking Takahashi.txt', 'r')
sys.stdin = f

X, K, D = map(int, input().split(' '))
X = abs(X)
if X >= K * D:
    print(X - K * D)
else:
    cnt = K - X // D
    X -= D * (X // D)
    if cnt % 2:
        print(abs(X - D))
    else:
        print(X)
