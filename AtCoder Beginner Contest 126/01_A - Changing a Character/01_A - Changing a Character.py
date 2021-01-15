import sys
import os
f = open('01_A - Changing a Character.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
S = list(input())
S[K-1] = S[K-1].lower()
for i in S:
    print(i, end='', sep='')