import sys
import os
f = open('03_C - Walk on Multiplication Table.txt', 'r')
sys.stdin = f

import math
N = int(input())
a = 0
for i in range(1, int(math.sqrt(N) // 1) + 1):
    a = max(a, math.gcd(i, N))
print(a + N // a - 2)
