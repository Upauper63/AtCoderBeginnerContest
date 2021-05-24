import sys
f = open('03_C - Ringos Favorite Numbers 2.txt', 'r')
sys.stdin = f

import collections
n = int(input())
rst = 0
a_ls = list(map(int, input().split(' ')))
for i in range(n):
    a_ls[i] %= 200
cnt_a_ls = collections.Counter(a_ls)
for k, v in cnt_a_ls.items():
    rst += (v * (v - 1)) // 2
print(rst)