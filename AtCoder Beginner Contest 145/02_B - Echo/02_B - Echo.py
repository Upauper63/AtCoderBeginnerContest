import sys
import os
f = open('02_B - Echo.txt', 'r')
sys.stdin = f

N = int(input())
S = input()
result = True
if N % 2 == 0:
    for i in range(N // 2):
        if S[i] != S[N // 2 + i]:
            result = False
            break
    if result:
        print('Yes')
    else:
        print('No')
else:
    print('No')