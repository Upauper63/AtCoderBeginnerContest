import sys
f = open('04_D - Staircase Sequences.txt', 'r')
sys.stdin = f

import math
n = int(input())
div_2n = []
for i in range(1, int(math.sqrt(2 * n)) + 1):
    if n * 2 % i == 0:
        j = 2 * n // i
        if i not in div_2n:
            div_2n.append(i)
        if j not in div_2n:
            div_2n.append(j)
rst = 0
for i in div_2n:
    if (i - 1 - 2 * n // i) % 2 == 0:
        rst += 1
print(rst)