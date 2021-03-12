
import sys
f =open('02.txt', 'r')
sys.stdin = f

import math
N = int(input())
ls = list(map(int, input().split(' ')))
val_1, val_2, val_3 = 0, 0, 0
for i in ls:
    val_1 += abs(i)
    val_2 += abs(i) ** 2
    val_3 = max(val_3, abs(i))
print(val_1)
print(math.sqrt(val_2))
print(val_3)
