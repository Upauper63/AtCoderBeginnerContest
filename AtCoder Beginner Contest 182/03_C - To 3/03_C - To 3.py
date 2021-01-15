import os
import sys
f = open('03.txt', 'r')
sys.stdin = f

ls = list(map(int, input()))
ls_1, ls_2 = [], []
if sum(ls) % 3 == 0:
    print(0)
    exit()

for i in ls:
    if i % 3 == 1:
        ls_1.append(i)
    elif i % 3 == 2:
        ls_2.append(i)
if sum(ls) % 3 == 2:
    if len(ls_2) >= 1 and len(ls) > 1:
        print(1)
        exit()
    elif len(ls_1) >= 2 and len(ls) > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()

if sum(ls) % 3 == 1:
    if len(ls_1) >= 1 and len(ls) > 1:
        print(1)
        exit()
    elif len(ls_2) >= 2 and len(ls) > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()