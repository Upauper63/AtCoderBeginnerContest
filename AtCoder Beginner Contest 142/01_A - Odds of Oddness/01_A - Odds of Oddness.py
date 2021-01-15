import sys
import os
f = open('01_A - Odds of Oddness.txt', 'r')
sys.stdin = f

import math
A = int(input())
print(math.ceil(A / 2) / A) 