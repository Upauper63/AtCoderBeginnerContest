import os
import sys
f = open('03_C - Snack.txt', 'r')
sys.stdin = f

import math
A, B = map(int, input().split(' '))
common = math.gcd(A, B)
print(A * B // common)