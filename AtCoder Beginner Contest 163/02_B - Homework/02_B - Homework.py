import sys
import os
f = open('02_B - Homework.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))

if sum(A_ls) > N:
    print(-1)
else:
    print(N - sum(A_ls))
        