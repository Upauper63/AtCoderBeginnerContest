import sys
f = open('01_A - Large Digits.txt', 'r')
sys.stdin = f

A, B = input().split(' ')
A = sum(map(int, list(A)))
B = sum(map(int, list(B)))
if A >= B:
    print(A)
else:
    print(B)