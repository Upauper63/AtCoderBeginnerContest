import sys
import os
f = open('01_A - Tenki.txt', 'r')
sys.stdin = f

S = input()
T = input()
cnt = 0
for i in range(3):
    if S[i] == T[i]:
        cnt += 1
print(cnt)