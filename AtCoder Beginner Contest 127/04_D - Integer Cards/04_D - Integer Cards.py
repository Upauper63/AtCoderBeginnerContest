import sys
f = open('04_D - Integer Cards.txt', 'r')
sys.stdin = f

from collections import deque
n, m = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort(reverse=True)
ls = deque(ls)
vals = []
for _ in range(m):
    b, c = map(int, input().split(' '))
    vals.append([b, c])
vals = sorted(vals, key=lambda x: x[1], reverse=True)
rst = 0
for val in vals:
    k, v = val
    cnt = 0
    while len(ls) > 0 and ls[-1] < v and cnt < k:
        d = ls.pop()
        rst += v
        cnt += 1
print(sum(ls) + rst)