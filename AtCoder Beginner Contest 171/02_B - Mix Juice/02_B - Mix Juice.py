import sys
import os
f = open('02_B - Mix Juice.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort()
print(sum(ls[:K]))
