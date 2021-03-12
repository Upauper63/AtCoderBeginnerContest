import sys

f = open('01_A - 9x9.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
if A > 9 or B > 9:
    print(-1)
else:
    print(A * B)