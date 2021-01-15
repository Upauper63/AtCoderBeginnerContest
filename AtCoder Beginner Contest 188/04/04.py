import os
import sys
f = open('04.txt', 'r')
sys.stdin = f

import  numpy as np
N, C = map(int, input().split(' '))
ls = np.zeros(10 ** 9 + 1)

# ls = [[] for i in range(10 ** 9 + 1)]
# ls = []
# for i in range(N):
#     a, b, c = map(int, input().split(' '))
#     ls[a] += c
#     ls[b + 1] -= c

print(np.sum(ls))
# for i in range(1, 10 ** 9 + 1):
#     ls[i + 1] += ls[i]
 
# for i in range(10 ** 9 + 1):
#     if ls[i] > C:
#         ls[i] = C

# print(ls.sum())
