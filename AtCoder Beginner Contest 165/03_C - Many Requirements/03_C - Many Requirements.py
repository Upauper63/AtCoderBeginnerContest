
import sys
f = open('03_C - Many Requirements.txt', 'r')
sys.stdin = f


import sys
f = open('03_C - Many Requirements.txt', 'r')
sys.stdin = f

import itertools
N, M, Q = map(int, input().split(' '))
ls = []
for i in range(Q):
    ls.append(list(map(int, input().split(' '))))
combis = itertools.combinations_with_replacement(range(1, M + 1), N)
rst = 0
for combi in combis:
    tmp = 0
    for a, b, c, d in ls:
        if combi[b - 1] - combi[a - 1] == c:
            tmp += d
    rst = max(rst, tmp)
print(rst)