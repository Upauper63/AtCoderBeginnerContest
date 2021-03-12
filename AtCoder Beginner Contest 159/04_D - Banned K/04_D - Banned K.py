
import sys
f = open('04_D - Banned K.txt', 'r')
sys.stdin = f

import collections
N = int(input())
ls = list(map(int, input().split(' ')))
cnt_dic = collections.Counter(ls)
cnt_ls = [0 for i in range(N + 1)]
for a, b in cnt_dic.items():
    cnt_ls[a] = (b * (b - 1) // 2)
sum_val = sum(cnt_ls)
for i in ls:
    if cnt_ls[i]:
        print(sum_val - (cnt_dic[i] - 1))
    else:
        print(sum_val)
