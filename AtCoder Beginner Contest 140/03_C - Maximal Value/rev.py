import os
import sys
f = open('03_C - Maximal Value.txt')
sys.stdin = f

N = int(input())
B_ls = [float('inf')] + list(map(int, input().split(' '))) + [float('inf')]
A_ls = [ [] for i in range(N) ]
for i in range(len(B_ls) - 1):
    A_ls[i] = min(B_ls[i], B_ls[i + 1])
print(sum(A_ls))