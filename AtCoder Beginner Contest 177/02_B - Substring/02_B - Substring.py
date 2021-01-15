import os
import sys
f = open('02_B - Substring.txt', 'r')
sys.stdin = f

S = input()
T = input()
rst = 0
for i in range(len(S) - len(T) + 1):
    idx = 0
    cnt = 0
    for j in range(i, i + len(T)):
        if S[j] == T[idx]: 
            cnt += 1
        idx += 1
    rst = max(rst, cnt)
print(len(T) - rst)