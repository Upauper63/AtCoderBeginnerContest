import os
import sys
f = open('03_C - To 3.txt', 'r')
sys.stdin = f

ls = list(map(int, input()))
rem_1_cnt, rem_2_cnt = 0, 0
if sum(ls) % 3 == 0:
    print(0)
    exit()

for i in ls:
    if i % 3 == 1:
        rem_1_cnt += 1
    elif i % 3 == 2:
        rem_2_cnt += 1


if sum(ls) % 3 == 1:
    if rem_1_cnt >= 1 and len(ls) > 1:
        print(1)
        exit()
    elif rem_2_cnt >= 2 and len(ls) > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()
else:
    if rem_2_cnt >= 1 and len(ls) > 1:
        print(1)
        exit()
    elif rem_1_cnt >= 2 and len(ls) > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()