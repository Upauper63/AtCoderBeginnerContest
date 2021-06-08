import sys
f = open('03_C - Friends and Travel costs.txt', 'r')
sys.stdin = f

import collections
n, k = map(int, input().split(' '))
dic = collections.defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split(' '))
    dic[a] += b
dic = sorted(dic.items())
val = k
for s, t in dic:
    if s > val:
        print(val)
        exit()
    val += t
if val >= 10 ** 100:
    print(10 ** 100)
else:
    print(val)