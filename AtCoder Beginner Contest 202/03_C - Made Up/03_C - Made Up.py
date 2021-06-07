import sys
f = open('03_C - Made Up.txt', 'r')
sys.stdin = f

import collections
n = int(input())
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
c_ls = list(map(int, input().split(' ')))
a_cnt_ls = collections.Counter(a_ls)
rst = 0
for i in c_ls:
    val = b_ls[i - 1]
    if val in a_cnt_ls:
        rst += a_cnt_ls[val]
print(rst)