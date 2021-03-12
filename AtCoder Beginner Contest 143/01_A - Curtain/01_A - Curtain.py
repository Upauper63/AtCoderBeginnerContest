import sys

f = open('01_A - Curtain.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
if A > B * 2:
    print(A - B * 2)
else:
    print(0)