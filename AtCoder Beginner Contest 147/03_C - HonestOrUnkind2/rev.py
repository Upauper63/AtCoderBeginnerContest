import os
import sys
f = open('03_C - HonestOrUnkind2.txt', 'r')
sys.stdin = f

N = int(input())
testimo_ls = [ [] for i in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        testimo_ls[i].append(tuple(map(int, input().split(' '))))
rst = 0
for i in range(1 << N):
    honest_ls = []
    for j in range(N):
        if i >> j & 1:
            honest_ls.append(j)
    is_ok = True
    for i in honest_ls:
        for testimo in testimo_ls[i]:
            if testimo[1] == 0 and (testimo[0] - 1) in honest_ls:
                is_ok = False
                break
            if testimo[1] == 1 and (testimo[0] - 1) not in honest_ls:
                is_ok = False
                break
    if is_ok:
        rst = max(rst, len(honest_ls))
print(rst)