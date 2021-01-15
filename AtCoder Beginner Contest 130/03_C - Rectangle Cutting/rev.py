import os
import sys
f = open('03_C - Rectangle Cutting.txt', 'r')
sys.stdin = f

W, H, x, y = map(float, input().split(' '))
if x == W / 2 and y == H / 2:
    print(W * H / 2, 1)
else:
    print(W * H / 2, 0)