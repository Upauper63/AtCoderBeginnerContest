
import sys
f = open('04_D - Div Game.txt', 'r')
sys.stdin = f

import math
N = int(input())
rst = 0
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i != 0:
        continue
    d = i
    while N % d == 0:
        rst += 1
        N //= d
        d *= i
    if N == 1:
        break
    while N % i == 0:
        N //= i
if N != 1:
    rst += 1
print(rst)