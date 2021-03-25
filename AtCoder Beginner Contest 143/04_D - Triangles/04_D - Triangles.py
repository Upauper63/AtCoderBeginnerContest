import sys
f = open('04_D - Triangles.txt', 'r')
sys.stdin = f

import bisect
n = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
rst = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = bisect.bisect_left(ls, ls[i] + ls[j])
        rst += k - j - 1
print(rst)