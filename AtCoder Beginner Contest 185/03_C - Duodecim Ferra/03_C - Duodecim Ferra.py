import os
import sys
f = open('03.txt', 'r')
sys.stdin = f

import math
N = int(input())
print(math.factorial(N - 1) // (math.factorial(N - 12) * math.factorial(11)))