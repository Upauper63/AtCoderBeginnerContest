import os
import sys
f = open('03_C - Sum of gcd of Tuples (Easy).txt', 'r')
sys.stdin = f

import math
K = int(input())
rst = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        tmp = math.gcd(i, j)
        for k in range(1, K + 1):
            rst += math.gcd(tmp, k)
print(rst)