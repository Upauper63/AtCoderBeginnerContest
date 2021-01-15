import os
import sys
f = open('03_C - Anti-Division.txt', 'r')
sys.stdin = f

import math
A, B, C, D = map(int, input().split(' '))
at_least_common = C * D // math.gcd(C, D)
except_nums = B // C - (A - 1) // C + B // D - (A - 1) // D - (B // at_least_common - (A - 1) // at_least_common)
print(B - (A - 1) - except_nums)
