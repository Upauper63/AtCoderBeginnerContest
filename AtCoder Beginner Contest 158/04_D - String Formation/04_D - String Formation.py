import os
import sys
f = open('04_D - String Formation.txt', 'r')
sys.stdin = f

import collections
S = collections.deque()
S.append(input())
Q = int(input())
is_reverse = 0
for i in range(Q):
    qu = input()
    if qu[:1] == '1':
        is_reverse = (is_reverse + 1) % 2
    else:
        qu_ls = list(qu.split(' '))
        if qu_ls[1] == '1':
            if is_reverse:
                S.append(qu_ls[2])
            else:
                S.appendleft(qu_ls[2])
        else:
            if is_reverse:
                S.appendleft(qu_ls[2])
            else:
                S.append(qu_ls[2])
if is_reverse:
    print(''.join(S)[::-1])
else:
    print(''.join(S))