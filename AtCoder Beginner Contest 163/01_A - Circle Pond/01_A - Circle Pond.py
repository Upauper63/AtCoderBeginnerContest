import sys
import os
f = open('01_A - Circle Pond.txt', 'r')
sys.stdin = f

import math
r = int(input())
print(2*r*math.pi)