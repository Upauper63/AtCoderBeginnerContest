import sys
import os
f = open('02_B - Tap Dance.txt', 'r')
sys.stdin = f

S = input()
odd_ls = ['R', 'U', 'D']
even_ls = ['L', 'U', 'D']
result = True
for i in range(len(S)):
    if i % 2 == 0 and S[i] not in odd_ls:
        result = False
    elif i % 2 == 1 and S[i] not in even_ls:
        result = False
if result:
    print('Yes')
else:
    print('No')