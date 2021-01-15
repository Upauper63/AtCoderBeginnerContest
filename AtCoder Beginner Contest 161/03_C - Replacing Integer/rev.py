import os
import sys
f = open('03_C - Replacing Integer.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
q = N // K
rst = min(N - K * q, K * (q + 1) - N)
print(rst)