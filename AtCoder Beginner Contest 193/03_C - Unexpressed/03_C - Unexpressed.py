
import sys
f = open('03_C - Unexpressed.txt', 'r')
sys.stdin = f

import math
N = int(input())
cnt = set()
for i in range(2, int(math.sqrt(N)) + 1):
    p = 2
    while i ** p <= N:
        cnt.add(i ** p)
        p += 1
print(N - len(cnt))