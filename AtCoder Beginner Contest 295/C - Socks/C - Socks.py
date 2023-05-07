import sys
f = open('C - Socks.txt', 'r')
sys.stdin = f

import collections
n = int(input())
ls = list(map(int, input().split(' ')))
cnt_ls = collections.Counter(ls)
cnt = 0
for i in cnt_ls.values():
    cnt += i // 2
print(cnt)