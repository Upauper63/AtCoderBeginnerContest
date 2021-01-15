import sys
import os
f = open('03_C - Maximal Value.txt', 'r')
sys.stdin = f

N = int(input())
B_ls = [float('inf')] + list(map(int, input().split(' '))) + [float('inf')]
A_ls = []
for i in range(N):
    A_ls.append(min(B_ls[i], B_ls[i + 1]))
print(sum(A_ls))