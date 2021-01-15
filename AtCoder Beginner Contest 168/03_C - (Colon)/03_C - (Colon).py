import sys
import os
f = open('03_C - (Colon).txt', 'r')
sys.stdin = f

import math
a, b, h, m = map(int, input().split(' '))

rec_h = 30 * h + 0.5 * m
rec_m = 6 * m
rec = abs(rec_h-rec_m)
if rec > 180:
    rec = 360 - rec

x = b * math.sin(math.radians(rec))
y = a - b * math.cos(math.radians(rec))

r = math.sqrt(x**2 + y**2)
print(r)