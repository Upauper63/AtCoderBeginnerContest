import sys
f = open('B - Counterclockwise Rotation.txt', 'r')
sys.stdin = f

import math
a, b, d = map(int, input().split(' '))
rad = math.radians(d)
x = a * math.cos(rad) - b * math.sin(rad)
y = b * math.cos(rad) + a * math.sin(rad)
print(x, y)