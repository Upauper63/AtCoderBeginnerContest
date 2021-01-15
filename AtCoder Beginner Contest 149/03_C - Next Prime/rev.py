import os
import sys
f = open('03_C - Next Prime.txt', 'r')
sys.stdin = f

import math
X = int(input())
is_end = False
if X == 2:
    print(X)
    exit()

while not is_end:
    is_end = True
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            is_end = False
            break
    if is_end:
        print(X)
        exit()
    X += 1