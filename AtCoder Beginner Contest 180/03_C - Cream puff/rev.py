import os
import sys
f = open('03_C - Cream puff.txt', 'r')
sys.stdin = f

import math
N = int(input())
ls = set()
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ls.add(i)
        ls.add(N // i)
ls = list(ls)
ls.sort()
[ print(i) for i in ls ]