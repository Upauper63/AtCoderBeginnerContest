import os
import sys
f = open('04_D - Floor Function.txt', 'r')
sys.stdin = f

from math import floor
A, B, N = map(int, input().split(' '))
rst = 0
if B <= N:
    x = B - 1
else:
    x = N
print(floor(A * x / B) - A * floor(x / B))