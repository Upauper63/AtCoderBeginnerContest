import os
import sys
f = open('03_C - (Colon).txt', 'r')
sys.stdin = f

import math
A, B, H, M = map(int, input().split(' '))
deg = abs(30 * H + 0.5 * M - 6 * M)
if deg > 180:
    deg = 360 - deg
rad = math.radians(deg)
print(math.sqrt((B - A * math.cos(rad)) ** 2 + (A * math.sin(rad)) ** 2))
