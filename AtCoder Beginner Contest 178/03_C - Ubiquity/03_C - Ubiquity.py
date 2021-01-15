import os
import sys
f = open('03_C - Ubiquity.txt', 'r')
sys.stdin = f

import math
N = int(input())
if N >= 2:
    print((10 ** N - (2 * 9 ** N - 8 ** N)) % (10 ** 9 + 7))
else:
    print(0)