import sys

f = open('03_C - Snack.txt', 'r')
sys.stdin = f

import math
A, B = map(int, input().split(' '))
print((A * B) // math.gcd(A, B))