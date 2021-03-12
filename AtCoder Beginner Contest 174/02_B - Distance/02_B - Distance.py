
import sys
f = open('02_B - Distance.txt', 'r')
sys.stdin = f

import math
N, D = map(int, input().split(' '))
rst = 0
for i in range(N):
    X, Y = map(int, input().split(' '))
    dist = math.sqrt(X ** 2 + Y ** 2)
    if dist <= D:
        rst += 1
print(rst)