import os
import sys
f = open('03_C - Exception Handling.txt', 'r')
sys.stdin = f

N = int(input())
val_1st, val_2nd = 0, 0
ls = []
for i in range(N):
    A = int(input())
    if val_1st < A:
        val_1st = A
    elif val_2nd < A:
        val_2nd = A
    ls.append(A)
for i in ls:
    if i != val_1st:
        print(val_1st)
    else:
        print(val_2nd)