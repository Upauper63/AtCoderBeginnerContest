
import sys
f = open('03.txt', 'r')
sys.stdin = f

import math
N = int(input())
ls = set()
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ls.add(i)
        ls.add(N // i)
[ print(i) for i in sorted(ls) ]