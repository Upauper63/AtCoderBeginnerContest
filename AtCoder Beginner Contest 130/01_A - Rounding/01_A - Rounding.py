import sys

f = open('01_A - Rounding.txt', 'r')
sys.stdin = f

X, A = map(int, input().split(' '))
if X < A:
    print(0)
else:
    print(10)