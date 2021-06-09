import sys
f = open('04_D - Opposite.txt', 'r')
sys.stdin = f

import math
n = int(input())
x, y = map(int, input().split(' '))
x_h, y_h = map(int, input().split(' '))
mid_x = (x_h + x) / 2
mid_y = (y_h + y) / 2
p0 = (x - mid_x) + (y - mid_y) * 1j
p1 = p0 * (math.cos(2 * math.pi/n) + math.sin(2 * math.pi/n) * 1j)
print(p1.real + mid_x, p1.imag + mid_y)