import sys
import os
f = open('03_C - Next Prime.txt', 'r')
sys.stdin = f

import math
X = int(input())
if X == 2:
    print(2)
else:
    is_find = False
    while not is_find:
        for i in range(2, X//2):
            is_find = True
            if math.gcd(X, i) != 1:
                is_find = False
                X += 1
                break
        rst = X
    print(rst)