import sys
f = open('03_C - Doubled.txt', 'r')
sys.stdin = f

import math
n = input()
n_len = len(n)
n = int(n)
rst = 0
for i in range(1, 10 ** (n_len // 2)):
    if i * 10 ** (math.log10(i) // 1 + 1) + i > n:
        break
    rst += 1
print(rst)
