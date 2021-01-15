import sys
import os
f = open('02_B - Minor Change.txt', 'r')
sys.stdin = f

S = list(input())
T = list(input())
cnt = 0
for s, t in zip(S, T):
    if s != t:
        cnt += 1
print(cnt)
