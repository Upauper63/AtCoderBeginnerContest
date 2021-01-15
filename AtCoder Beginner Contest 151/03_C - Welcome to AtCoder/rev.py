import os
import sys
f = open('03_C - Welcome to AtCoder.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
ac_ls = []
wa_cnt = 0
for i in range(M):
    p, s = input().split(' ')
    p = int(p)
    if p not in ac_ls:
        if s == 'AC':
            ac_ls.append(p)
        else:
            wa_cnt += 1
print(len(ac_ls), wa_cnt)