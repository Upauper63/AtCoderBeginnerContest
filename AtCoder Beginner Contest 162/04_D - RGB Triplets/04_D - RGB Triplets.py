
import sys
f = open('04_D - RGB Triplets.txt', 'r')
sys.stdin = f

import collections
N = int(input())
S = list(input())
cnt_ls = collections.Counter(S)
rst = 1
if len(cnt_ls) < 3:
    print(0)
    exit()
for i in cnt_ls.values():
    rst *= i
for d in range(1, N):
    for i in range(N):
        j = i + d
        k = j + d
        if k >= N:
            break
        if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            rst -= 1
print(rst)