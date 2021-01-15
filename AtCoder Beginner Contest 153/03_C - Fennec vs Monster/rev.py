import os
import sys
f = open('03_C - Fennec vs Monster.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort(reverse=True)
print(sum(ls[K:]))