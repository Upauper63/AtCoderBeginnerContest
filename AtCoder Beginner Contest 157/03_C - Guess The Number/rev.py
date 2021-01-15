import os
import sys
f = open('03_C - Guess The Number.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
if N == 1:
    if M == 0:
        print(0)
        exit()
    rst = ''
    for i in range(M):
        s, c = map(int, input().split(' '))
        if s != 1:
            print(-1)
            exit()
        if not rst:
            rst = c
        elif rst != c:
            print(-1)
            exit()
    print(rst)

else:
    ls = [ [] for i in range(N) ]
    for i in range(M):
        s, c = map(int, input().split(' '))
        if s == 1 and c == 0:
            print(-1)
            exit()
        if not ls[s - 1]:
            ls[s - 1] = c
        elif ls[s - 1] != c:
            print(-1)
            exit()
    for idx, val in enumerate(ls):
        if not val:
            if idx == 0:
                print(1, end='')
            else:
                print(0, end='')
        else:
            print(val, end='')