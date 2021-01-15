import os
import sys
f = open('04_D - Leaping Tak.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = [0 for i in range(N * 2 + 1)]
ls[0] = 1
ls[1] -= 1
S = set()
for i in range(K):
    l, r = map(int, input().split(' '))
    S.add((l, r))
for i in range(N):
    for l, r in S:
        ls[i + l] += ls[i]
        ls[i + r + 1] -= ls[i]
    ls[i + 1] = (ls[i] + ls[i + 1]) % 998244353
print(ls[N - 1])
