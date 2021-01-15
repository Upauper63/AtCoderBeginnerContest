import sys
import os
f = open('03_C - Distinct or Not.txt', 'r')
sys.stdin = f

N = int(input())
A_ls = input().split(' ')
rst = { i for i in A_ls }
if N == len(rst):
    print('YES')
else:
    print('NO')
