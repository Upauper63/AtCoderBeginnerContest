import os
import sys
f = open('04_D - Stamp.txt', 'r')
sys.stdin = f

import math
N, M = map(int, input().split(' '))

if M == 0:
    print(1)
    exit()

ls = list(map(int, input().split(' '))) + [0, N + 1]
ls.sort()
segs = []
for i in range(1, M + 2):
    segs.append(ls[i] - ls[i - 1] - 1)

segs.sort(reverse=True)

while len(segs) > 0 and segs[-1] == 0:
    segs.pop()

if len(segs) == 0:
    print(0)
    exit()

max_size = segs[-1]
rst = 0
for seg in segs:
    rst += math.ceil(seg / max_size)
print(rst)