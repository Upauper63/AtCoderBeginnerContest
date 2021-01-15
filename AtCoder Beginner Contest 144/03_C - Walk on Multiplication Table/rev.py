import os
import sys
f = open('03_C - Walk on Multiplication Table.txt', 'r')
sys.stdin = f

import math
N = int(input())
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        a = i
        b = N // i
print(a - 1 + b - 1)