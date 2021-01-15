import os
import sys
f = open('03_C - Forbidden List.txt', 'r')
sys.stdin = f

X, N = map(int, input().split(' '))
if N == 0:
    print(X)
else:
    ls = list(map(int, input().split(' ')))
    diff = float('inf')
    rst = float('inf')
    cnt = 0
    is_end = False
    while not is_end:
        if cnt not in ls:
            if diff < abs(X - cnt):
                is_end = True
                print(rst)
                exit()
            if diff == abs(X - cnt):
                rst = min(rst, cnt)
            else:
                diff = min(abs(X - cnt), diff)
                if diff == abs(X - cnt):
                    rst = cnt
        cnt += 1