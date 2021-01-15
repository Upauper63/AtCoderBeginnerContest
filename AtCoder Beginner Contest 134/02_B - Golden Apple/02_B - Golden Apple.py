import sys
import os
f = open('02_B - Golden Apple.txt', 'r')
sys.stdin = f

import math
N, D = map(int, input().split(' '))
print(math.ceil(N / (D * 2 + 1)))