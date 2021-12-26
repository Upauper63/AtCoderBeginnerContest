import sys
f = open('03_C - Product.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)
from collections import Counter
n, x = map(int, input().split(' '))
ls_clusters = []
counter = []
for _ in range(n):
    val = list(map(int, input().split(' ')))[1:]
    ls_clusters.append(set(val))
    counter.append(Counter(val))

rst = 0

def recur(val, idx, tmp):
    global rst
    if idx == n - 1:
        for i in ls_clusters[idx]:
            if val == i:
                tmp *= counter[idx][i]
                rst += tmp
    else:
        for i in ls_clusters[idx]:
            if val % i == 0 and val // i > 0:
                recur(val // i, idx + 1, tmp * counter[idx][i])
    return

for i in ls_clusters[0]:
    if x % i == 0 and x // i > 0:
        val = x // i
        tmp = counter[0][i]
        recur(val, 1, tmp)

print(rst)

