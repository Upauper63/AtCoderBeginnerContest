import sys
f = open('04_D - Water Bottle.txt', 'r')
sys.stdin = f

import math
a, b, x = map(int, input().split(' '))
if a ** 2 * b / 2 >= x:
    y = 2 * x / (a * b)
    print(math.degrees(math.atan(b / y)))
else:
    x = a ** 2 * b - x
    y = 2 * x / a ** 2
    print(math.degrees(math.atan(y / a)))