import sys
import os
f = open('02_B - Popular Vote.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
A_ls = [i for i in A_ls if i >=  sum(A_ls)  / (4 * M)]

if len(A_ls) >= M:
    print('Yes')
else:
    print('No')