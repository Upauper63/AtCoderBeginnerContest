import sys
import os
f = open('02_B - Trick or Treat.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = [0] * N
for i in range(K):
    d = int(input())
    tmp_ls = map(int, input().split(' '))
    for j in tmp_ls:
        ls[j-1] += 1
print(ls.count(0))