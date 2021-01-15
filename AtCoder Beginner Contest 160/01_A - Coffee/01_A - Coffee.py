import sys
import os
f = open('01_A - Coffee.txt', 'r')
sys.stdin = f

S = input()
if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')