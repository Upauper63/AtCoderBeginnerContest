import sys
f = open('A - A to Z String 2.txt', 'r')
sys.stdin = f

import math
n, x = map(int, input().split(' '))
print(chr(ord('A') -1 + math.ceil(x / n)))