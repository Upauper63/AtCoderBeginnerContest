import sys
import os
f = open('01_A - Takoyaki.txt', 'r')
sys.stdin = f

import math
N, X, T = map(int, input().split(' '))
print(math.ceil(N / X) * T)