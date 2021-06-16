
import sys
f = open('04_D - Snuke Prime.txt', 'r')
sys.stdin = f

import collections
n, c = map(int, input().split(' '))
dic = collections.defaultdict(int)
for _ in range(n):
    a, b, ci = map(int, input().split(' '))
    dic[a] += ci
    dic[b + 1] -= ci
dic = sorted(dic.items())
prev_day = dic[0][0]
val = dic[0][1]
rst = 0
for k, v in dic[1:]:
    if val > c:
        rst += c * (k - prev_day)
    else:
        rst += val * (k - prev_day)
    prev_day = k
    val += v
print(rst)