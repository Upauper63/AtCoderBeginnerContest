import sys

f = open('01_A - AC or WA.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
if N == M:
    print('Yes')
else:
    print('No')