import sys
import os
f = open('01_A - Serval vs Monster.txt', 'r')
sys.stdin = f

import math
H, A = map(int, input().split(' '))
print(math.ceil(H / A))