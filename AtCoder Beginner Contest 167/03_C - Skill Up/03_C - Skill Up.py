import sys
import os
f =open('03_C - Skill Up.txt', 'r')
sys.stdin = f

N, M, X = map(int, input().split(' '))
price, exp, rst = [], [], -1
for i in range(N):
    ls = list(map(int, input().split(' ')))
    price.append(ls[0])
    exp.append(ls[1:])
for i in range(1 << N):
    price_combi, exp_combi, exp_rst, cnt = [], [], [0] * M, []
    for j in range(N):
        if (i >> j) & 1:
            price_combi.append(price[j])
            exp_combi.append(exp[j])
    for s in range(len(exp_combi)):
        for t in range(M):
            exp_rst[t] += exp_combi[s][t]
    [cnt.append(i) for i in exp_rst if i >= X]
    if len(cnt) == M:
        if rst == -1:
            rst = sum(price_combi)
        else:
            rst = min(rst, sum(price_combi))
print(rst)