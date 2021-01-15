import sys
import os
f = open('03_C - Sum of gcd of Tuples (Easy).txt', 'r')
sys.stdin = f

import math
rst = 0
K = int(input())
for i in range(1, K + 1):
    for j in range(1, K + 1):
        tmp = math.gcd(i, j)
        for k in range(1, K + 1):
            rst += math.gcd(tmp, k)
print(rst)