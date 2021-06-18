import sys
f = open('04_D - Kth Excluded.txt', 'r')
sys.stdin = f

import bisect
n, q = map(int, input().split(' '))
a_ls = [0] + list(map(int, input().split(' ')))
ls = []
val = 0
for i in range(n):
    val += a_ls[i + 1] - a_ls[i] - 1
    ls.append(val)

for _ in range(q):
    k = int(input())
    if k > ls[-1]:
        print(a_ls[-1] + k - ls[-1])
    else:
        idx = bisect.bisect_left(ls, k)
        if idx > 0:
            print(a_ls[idx] + k - ls[idx - 1])
        else:
            print(a_ls[idx] + k)