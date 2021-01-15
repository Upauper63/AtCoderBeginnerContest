import os
import sys
f = open('03_C - Poll.txt', 'r')
sys.stdin = f

N = int(input())
rst = {}
for i in range(N):
    val = input()
    if val in rst:
        rst[val] += 1
    else:
        rst[val] = 1
rst = sorted(rst.items(), key=lambda x:x[1], reverse=True)
max_cnt = rst[0][1]
ls = []
[ ls.append(i[0]) for i in rst if i[1] == max_cnt ]
[ print(i) for i in sorted(ls) ]
