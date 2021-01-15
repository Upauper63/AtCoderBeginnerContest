import sys
import os
f = open('03_C - Fennec vs Monster.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
H_ls = list(map(int, input().split(' ')))
H_ls.sort(reverse=True)
print(sum(H_ls[K:]))