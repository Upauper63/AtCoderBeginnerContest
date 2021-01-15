import os
import sys
f = open('02.txt', 'r')
sys.stdin = f

sx, sy, gx, gy = map(float, input().split(' '))
print(sx + sy * (gx - sx) / (gy + sy))