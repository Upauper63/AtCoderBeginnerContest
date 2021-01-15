import os
import sys
f = open('03_C - Divide the Problems.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
print(ls[N // 2] - ls[N // 2 - 1])