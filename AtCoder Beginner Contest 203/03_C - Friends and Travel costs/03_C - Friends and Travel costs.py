import sys
f = open('03_C - Friends and Travel costs.txt', 'r')
sys.stdin = f

import collections
n, k = map(int, input().split(' '))
dic = collections.defaultdict(int)
for i in range(n):
    a, b = map(int, input().split(' '))
    dic[a] += b
dic = sorted(dic.items())
cumsum_dic = {}
val = 0
for t in dic:
    val += t[1]
    cumsum_dic[t[0]] = val
max_val = 0
for s, t in cumsum_dic.items():
    if s - 1 >= max_val + k:
        print(k + max_val)
        exit()
    if k + t < s:
        print(k + t)
        exit()
    max_val = t
if 10 ** 100 <= k + max_val:
    print(10 ** 100)
else:
    print(k + max_val)